
from rlpyt.agents.pg.categorical import (CategoricalPgAgent,
    RecurrentCategoricalPgAgent, AlternatingRecurrentCategoricalPgAgent)
from rlpyt.models.pg.grid_ff_model import GridFfModel, GridBasisModel


class GridMixin:

    def make_env_to_model_kwargs(self, env_spaces):
        return dict(image_shape=env_spaces.observation.shape,
                    output_size=env_spaces.action.n)


class GridFfAgent(GridMixin, CategoricalPgAgent):

    def __init__(self, ModelCls=GridFfModel, **kwargs):
        super().__init__(ModelCls=ModelCls, **kwargs)


class GridBasisAgent(GridMixin, CategoricalPgAgent):   #EDIT# GridBasisModel Ctrl+Click하기

    def __init__(self, ModelCls=GridBasisModel, **kwargs):   #EDIT# 어차피 키워드 인자는 그대로 전달됨
        super().__init__(ModelCls=ModelCls, **kwargs)


