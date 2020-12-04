
from OTMWrapper import OTMWrapper

start_time = 0.
duration = 3600.
advance_time = 300.

# load the configuration file
name = 'berkeley_large.xml'
otm = OTMWrapper(name)

# initialize (prepare/rewind the simulation)
otm.initialize(1.)

# run step-by-step using the 'advance' method
time = start_time
end_time = start_time + duration

while(time<end_time):
  otm.advance(advance_time)

  # Insert your code here -----
  print(otm.otm.get_current_time())
  time += advance_time;
  print(otm.get_links_table())


# always end by deleting the wrapper
print(otm.to_networkx())
del otm
