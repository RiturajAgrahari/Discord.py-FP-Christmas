from models import Profile


async def get_data():
    profiles = await Profile.all()
    with open("data.txt", "a") as f:
        f.truncate(0)
        f.write(f"{'id'.center(6)} | {'discord_id'.center(30)} | {'discord_name'.center(50)} \n")
        f.write(f"-------+--------------------------------+----------------------------------------------------"
                f"----------\n")
        for i in range(0, len(profiles)):
            f.write(f"{str(profiles[i].id).center(6)} | {str(profiles[i].discord_id).center(30)} |"
                    f" {str(profiles[i].discord_name).center(50)}\n")

