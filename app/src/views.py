import pandas as pd
from fastapi import APIRouter, status, HTTPException
from .schemas import Distribution
from .utils import dist


router = APIRouter(tags=['distribution'])


@router.get("/", status_code=status.HTTP_200_OK)
async def main():
    return 'Send me statistics parameters, I will generate cause and effect in given range with acceptable correlation'


@router.post("/", status_code=status.HTTP_201_CREATED)
async def distribution_generator(distribution: Distribution):
    """
    This will generate a column (cause) with specified statistic properties and then will try to 
    create an effect as the second column in the acceptable correlation with the first column
    """
    df = pd.DataFrame()

    try:
        model = dist(distribution.min, distribution.max, distribution.mean, distribution.std)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Sorry! Cannot create distribution for the given parameters...'
        )

    cause = model.rvs(size=distribution.samples)
    df['Cause'] = cause

    tolerance = 0.1

    while True:
        # generate random data with given statistics, until achieving 
        # an acceptable correlation between cause and effect
        df['Effect'] = model.rvs(size=distribution.samples)
        correlation = df['Effect'].corr(df['Cause'])
        if (distribution.corr - tolerance < correlation < distribution.corr + tolerance):
            break

    return {'statistics': df.describe().transpose(), 'data': df}





