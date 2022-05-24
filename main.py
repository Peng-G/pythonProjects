import cProfile
import pstats

cProfile.run('product(1,2)','my_math.profile')

p = pstats.Stats('my_math.profile')