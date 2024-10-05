"""create table

Revision ID: 1f1cc2b2494d
Revises: 0c0845b70ee2
Create Date: 2024-10-02 17:25:51.931253

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1f1cc2b2494d"
down_revision: Union[str, None] = "0c0845b70ee2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
