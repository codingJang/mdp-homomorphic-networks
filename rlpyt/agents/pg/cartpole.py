

from rlpyt.agents.pg.categorical import (CategoricalPgAgent,
    RecurrentCategoricalPgAgent, AlternatingRecurrentCategoricalPgAgent)
from rlpyt.models.pg.cartpole_ff_model import CartpoleFfModel, \
    CartpoleBasisModel


class CartpoleMixin:

    def make_env_to_model_kwargs(self, env_spaces):
        return dict(image_shape=env_spaces.observation.shape,
                    output_size=env_spaces.action.n)


class CartpoleFfAgent(CartpoleMixin, CategoricalPgAgent):

    def __init__(self, ModelCls=CartpoleFfModel, **kwargs):
        super().__init__(ModelCls=ModelCls, **kwargs)

class CartpoleBasisAgent(CartpoleMixin, CategoricalPgAgent):  #EDIT# CartpoleBasisModel Ctrl+Click하기

    def __init__(self, ModelCls=CartpoleBasisModel, **kwargs):  #EDIT# 어차피 키워드 인자는 그대로 전달됨
        super().__init__(ModelCls=ModelCls, **kwargs)
