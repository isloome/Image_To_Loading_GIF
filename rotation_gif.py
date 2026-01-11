from PIL import Image

img_path ="/path/to/your_photo"
img = Image.open(img_path).convert("RGBA")
#scale
scale_factor = 1.00
new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
img = img.resize(new_size, Image.LANCZOS)

#canvas
canvas_size = max(256, 256)
base_canvas = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
base_canvas.paste(
    img,
    ((canvas_size - new_size[0]) // 2, (canvas_size - new_size[1]) // 2),
    img
)

#rotation frames
frames = []
frame_count = 48
duration = 30  #ms

for i in range(frame_count):
    angle = (360 / frame_count) * i
    frame = base_canvas.rotate(-angle, resample=Image.BICUBIC, expand=False)
    frames.append(frame)

output_path = "/path/to/save.gif"
frames[0].save(
    output_path,
    save_all=True,
    append_images=frames[1:],
    duration=duration,
    loop=0,
    disposal=2
)

output_path
