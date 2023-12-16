import os
from datasets import load_dataset

# Define the base directory where the script is located
base_dir = os.path.dirname(os.path.realpath(__file__))


config = "common_crawl"
# Define the path to save each configuration
config_path = os.path.join(base_dir, "RedPajama-Data-V2", config)
# cache_dir is conig_path/cache_dir
cache_dir = os.path.join(config_path, "cache_dir")

# Ensure the directory exists
os.makedirs(config_path, exist_ok=True)
# create cache_dir
os.makedirs(cache_dir, exist_ok=True)

while True:
        # Attempt to load the dataset with the specified configuration
        try:
            # ds = load_dataset("togethercomputer/RedPajama-Data-V2", config, cache_dir=cache_dir)

            ds = load_dataset(
                            "togethercomputer/RedPajama-Data-V2", 
                            partition="head_middle",
                            # partition="tail",
                            snapshots=["2023-14"], 
                            languages=["en"], 
                            name="default",
                            cache_dir=cache_dir
                        )

            input(f"Dataset '{config}' configuration loaded successfully. Press Enter to save it to -------------------------------------------------->>>>> {config_path}")

            # ask for confirmation to save in the path or give a new path
            new_path = input("Press Enter to save it to the path above or enter a new path: ")
            # /Volumes/T7 SHIELD/Hugging Face datasets/RedPajama-Data-V2/c4
            if new_path != "":
                config_path = new_path
                os.makedirs(config_path, exist_ok=True)
                os.makedirs(os.path.join(config_path, "cache_dir"), exist_ok=True)
                print(f"Dataset '{config}' configuration will be saved to {config_path}")
                input("confirm to save to the path above. Press Enter to continue...")


            # Save the dataset to the specified path
            ds.save_to_disk(config_path)
            print(f"Dataset '{config}' configuration saved to {config_path}")
            
            # not shure if this works
            ds.cleanup_cache_files()
            print(f"Dataset '{config}' configuration cache cleaned up")

            # Exit the loop
            break

        except Exception as e:
            print(f"\n\n\nAn error occurred while processing the '{config}' configuration: {e}\n\n\n")
else:
    print("config not found")
