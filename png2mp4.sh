ffmpeg -y -r 5 -i svgs/from_sfen%03d.png -pix_fmt yuv420p -f mp4 out.mp4 && xdg-open out.mp4
