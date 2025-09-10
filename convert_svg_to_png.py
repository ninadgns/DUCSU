import os
import cairosvg

input_folder = 'Charts'
output_folder = 'charts_png'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.svg'):
        svg_path = os.path.join(input_folder, filename)
        png_path = os.path.join(output_folder, filename.rsplit('.', 1)[0] + '.png')
        cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=2000)
        print(f"Converted {filename} to {png_path}")