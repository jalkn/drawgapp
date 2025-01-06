from moviepy.editor import VideoFileClip

def split_video(input_path, output_path1, output_path2, split_time):

    try:
        clip = VideoFileClip(input_path)
        duration = clip.duration

        if split_time <= 0 or split_time >= duration:
            raise ValueError("Split time must be between 0 and the video duration.")

        clip1 = clip.subclip(0, split_time)
        clip2 = clip.subclip(split_time, duration)

        clip1.write_videofile(output_path1, codec="libx264", audio_codec="aac") # Use appropriate codecs
        clip2.write_videofile(output_path2, codec="libx264", audio_codec="aac")

    except OSError as e:
        print(f"Error reading or writing video file: {e}")
    except ValueError as e:
        print(f"Invalid split time: {e}")
    except Exception as e: # Catching other potential exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        # Important: Close the clip to release resources.
        if 'clip' in locals():
          clip.close()

# Example usage:
input_video = "../src/heroINA/laHero.mp4"  
output_video1 = "src/hero1.mp4"
output_video2 = "src/hero2.mp4"
split_point = 200

split_video(input_video, output_video1, output_video2, split_point) 