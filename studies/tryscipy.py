import scipy
import scipy.constants



print(dir(scipy.constants))

a  = scipy.constants.c
print(a)

b  = scipy.constants.speed_of_light
c = scipy.constants.speed_of_sound

print(f"the speed of light is:{b}m/s, ")
print(f"the speed of light is:{b/1000}km/s, ")
print(f"the speed of sound is:{c}")


d = scipy.constants.physical_constants["alpha particle mass"]
print(f"physical_constants is: {d[0:]}")
print(scipy.__version__)
