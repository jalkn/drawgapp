import subprocess

def convert_mov_to_mp4_subprocess(mov_path, mp4_path):
    try:
        cmd = [
            'ffmpeg',
            '-i', mov_path,
            '-vcodec', 'libx264',  # Video codec
            '-acodec', 'aac',    # Audio codec
            '-y',               # Overwrite output if it exists
            mp4_path
        ]
        subprocess.run(cmd, check=True)  # check=True raises an exception on error
        print(f"Successfully converted {mov_path} to {mp4_path}")
    except FileNotFoundError:
        print(f"Error: Input file '{mov_path}' not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error converting video: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

mov_file = "../src/norst.mov"
mp4_file = "../src/norst.mp4"
convert_mov_to_mp4_subprocess(mov_file, mp4_file)