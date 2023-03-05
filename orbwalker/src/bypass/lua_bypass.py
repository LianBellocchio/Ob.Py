import subprocess

class LuaBypass:
    def __init__(self, lua_script_path):
        self.lua_script_path = lua_script_path
    
    def execute_lua_script(self, script_args):
        command = ['lua', self.lua_script_path] + script_args
        output = subprocess.check_output(command)
        return output.decode('utf-8')
