from pydantic import BaseModel, Field, validator


class Distribution(BaseModel):
    min: float = Field(title="Minimum value in the distributed range", ge=0, default=0)
    max: float = Field(title="Maximum value in the distributed range", default=100)
    mean: float = Field(title="Mean", default=50)
    std: float = Field(title="Standard divination", default=10)
    corr: float = Field(title="Expected correlation between Cause and Effect", ge=0.1, le=0.9, default=0.5)
    samples: int = Field(title="Number of samples", gt=0, default=50)
