import subprocess

def convert_4k_to_fullhd(input_file, output_file):

    try:
        command = [
            "ffmpeg",
            "-i", input_file,  # Input file
            "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease",  # Scale to 1920x1080, maintain aspect ratio
            "-c:v", "libx264",  # Use x264 encoding (good quality/size trade-off)
            "-preset", "medium",  # Encoding speed/quality preset (adjust as needed)
            "-crf", "23",  # Constant rate factor (quality control, lower=better, higher=smaller file size)
            "-c:a", "copy",  # Copy audio codec (avoids re-encoding if possible)
            "-movflags", "+faststart",  # Optimize for web playback
            output_file  # Output file
        ]


        # Execute the command
        subprocess.run(command, check=True)  # check=True raises an exception if the command fails

        print(f"Successfully converted {input_file} to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file {input_file} not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error: ffmpeg conversion failed: {e}")


# Example 1: Converting input.mp4 to output.mp4
input_file = "../src/norst4k.mp4"
output_file = "src/norstFHD.mp4"
convert_4k_to_fullhd(input_file, output_file)
