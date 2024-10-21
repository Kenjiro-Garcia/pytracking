import os
import sys
import argparse
import json

env_path = os.path.join(os.path.dirname(__file__), '..')
if env_path not in sys.path:
    sys.path.append(env_path)

from pytracking.evaluation import Tracker

def run_video(tracker_name, tracker_param, videofile, bbox_dict=None, crop_params=None, debug=None, save_results=False, show_display=False):
    """Run the tracker on your webcam.
    args:
        tracker_name: Name of tracking method.
        tracker_param: Name of parameter file.
        debug: Debug level.
    """
    tracker = Tracker(tracker_name, tracker_param)
    tracker.run_video_generic(videofilepath=videofile, bbox_dict=bbox_dict, crop_params=crop_params, debug=debug, save_results=save_results, show_display=show_display)

def main():
    parser = argparse.ArgumentParser(description='Run the tracker on your video file.')
    parser.add_argument('tracker_name', type=str, help='Name of tracking method.')
    parser.add_argument('tracker_param', type=str, help='Name of parameter file.')
    parser.add_argument('videofile', type=str, help='Path to a video file.')
    parser.add_argument('--bbox_file', type=str, default=None, help='LabelBee JSON file.')
    parser.add_argument('--crop_params', type=float, default=None, nargs="+", help='X Y coordinates transformations for cropped video')
    parser.add_argument('--debug', type=int, default=0, help='Debug level.')
    parser.add_argument('--save_results', dest='save_results', action='store_true', help='Save bounding boxes')
    parser.add_argument('--show_display', action='store_true', help='If option is added, it will open display window')
    parser.set_defaults(save_results=False)

    args = parser.parse_args()

    with open(args.bbox_file, 'r') as b:
        b_file = json.load(b)

    run_video(args.tracker_name, args.tracker_param, args.videofile, b_file, args.crop_params, args.debug, args.save_results, args.show_display)

if __name__ == '__main__':
    main()