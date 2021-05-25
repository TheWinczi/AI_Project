
# constants values representing fields in the game world
EMPTY_FIELD_VALUE = 0
OBSTACLE_VALUE = 1
AGENT_VALUE = 2
DESTINATION_VALUE = 3
PATH_VALUE = 4

OBSTACLE_CHAR = "#"
DESTINATION_CHAR = "$"
AGENT_CHAR = "A"
EMPTY_FIELD_CHAR = "."
PATH_CHAR = "X"

# constants values representing game world building
OBSTACLES_COUNT = 15
MIN_OBSTACLE_HEIGHT = 1
MIN_OBSTACLE_WIDTH = 1
MAX_OBSTACLE_SIZE = 4

# constants values representing agent parameters
EXPLORATION_RATE_INIT = 1
EXPLORATION_DECAY_RATE = 0.999
LEARNING_RATE = 0.1
DISCOUNT_RATE = 0.999
MAX_AGENT_MOVES_COUNT = 150

# constants values representing fields costs
EMPTY_FIELD_COST = -3
DESTINATION_FIELD_PRICE = 30
INIT_DECISION_RATING = 10


