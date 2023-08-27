import config as c
import assim_tools

s_dir = f'/s{c.scale+1}' if c.nscale>1 else ''

prior_state_file = c.work_dir+'/analysis/'+c.time+s_dir+'/prior_state.bin'
post_state_file = c.work_dir+'/analysis/'+c.time+s_dir+'/post_state.bin'
obs_seq_file = c.work_dir+'/analysis/'+c.time+s_dir+'/obs_seq.bin'

comm = assim_tools.parallel_start()

# assim_tools.process_state(c, comm, prior_state_file)

# assim_tools.process_obs(c, comm, obs_seq_file)

assim_tools.local_analysis(c, comm, prior_state_file, post_state_file, obs_seq_file)

# assim_tools.update_restart(c, comm, prior_state_file, post_state_file)

