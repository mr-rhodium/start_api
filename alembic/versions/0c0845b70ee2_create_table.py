"""create table

Revision ID: 0c0845b70ee2
Revises: 460b61ca1573
Create Date: 2024-10-02 17:11:53.525280

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0c0845b70ee2"
down_revision: Union[str, None] = "460b61ca1573"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
