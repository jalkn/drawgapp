import subprocess

def convert_fullhd_to_hd(input_file, output_file):

    try:
        command = [
            "ffmpeg",
            "-i", input_file,  # Input file
            "-vf", "scale=1280:720:force_original_aspect_ratio=decrease",  # Scale to 1280x720 (720p), maintain aspect ratio
            "-c:v", "libx264",  # Use x264 encoding 
            "-preset", "medium",  # Encoding speed/quality preset
            "-crf", "23",  # Constant rate factor (adjust as needed)
            "-c:a", "aac",       # Re-encode audio to AAC (common for HD)
            "-b:a", "128k",      # Audio bitrate (adjust as needed) 
            "-movflags", "+faststart", # Optimize for web playback
            output_file  # Output file
        ]

        subprocess.run(command, check=True)

        print(f"Successfully converted {input_file} to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file {input_file} not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error: ffmpeg conversion failed: {e}")


# Example usage:
input_file = "../src/norst.mp4"
output_file = "src/norstHD.mp4"
convert_fullhd_to_hd(input_file, output_file)