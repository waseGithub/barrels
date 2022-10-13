from RsNgx import *

# Use the instr_list string items as resource names in the RsNgx constructor
instr_list = RsNgx.list_resources("?*")
print(instr_list)