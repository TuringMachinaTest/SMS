from dateutil.relativedelta import relativedelta

from psqlextra.partitioning import (
    PostgresPartitioningManager,
    PostgresCurrentTimePartitioningStrategy,
    PostgresTimePartitionSize,
    partition_by_current_time,
)
from psqlextra.partitioning.config import PostgresPartitioningConfig

from .models import RawEvent, DecryptedEvent

manager = PostgresPartitioningManager([
    # 3 partitions ahead, each partition is one month
    # delete partitions older than 6 months
    # partitions will be named `[table_name]_[year]_[3-letter month name]`.
    PostgresPartitioningConfig(
        model=RawEvent,
        strategy=PostgresCurrentTimePartitioningStrategy(
            size=PostgresTimePartitionSize(months=1),
            count=120,
            #max_age=relativedelta(months=6),
        ),
    ),
    PostgresPartitioningConfig(
        model=DecryptedEvent,
        strategy=PostgresCurrentTimePartitioningStrategy(
            size=PostgresTimePartitionSize(months=1),
            count=120,
            #max_age=relativedelta(months=6),
        ),
    ),
])