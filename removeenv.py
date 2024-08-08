import subprocess

def remove_all_envs():
    envs = subprocess.check_output(["conda", "env", "list", "--json"]).decode("utf-8")
    print("envs", envs)
    import json
    envs_dict = json.loads(envs)
    for env in envs_dict['envs']:
        if env != envs_dict['default_prefix']:
            env=env.split("/")[-1]
            subprocess.run(["conda", "remove", "-n", env, "--all"])

remove_all_envs()
