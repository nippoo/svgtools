import os, fnmatch, re

def findreplace():
    for path, dirs, files in os.walk(os.getcwd()):
        for filename in (fnmatch.filter(files, "*.svg") + fnmatch.filter(files, "*.SVG")):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()

                # replace rgba(r,g,b,1) with rgb(r,g,b)
                s = re.sub(r'rgba\(([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),1\)', r'rgb(\1,\2,\3)', s)

                # replace non-opaque colours with fill-opacity
                s = re.sub(r'fill: rgba\(([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9])\)', r'fill:rgb(\1,\2,\3);fill-opacity:\4', s)

                # replace non-opaque stroke colours with stroke-opacity
                s = re.sub(r'stroke: rgba\(([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9])\)', r'stroke:rgb(\1,\2,\3);stroke-opacity:\4', s)

                # replace rgba(white) with white
                s = s.replace("rgb(255,255,255)", "#fff")

                # replace rgb(r,g,b) tuplets with black
                s = re.sub(r'rgb\(([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9])\)', r'#000', s)

                # replace all strokes with black strokes
                s = re.sub(r'stroke:#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})', r'stroke:#000', s)

                # font replacement for Illustrator etc
                s = s.replace("font-family: sans-serif", "font-family: Arial")

            fix_filepath = os.path.join(path, "blackened_" + filename)
            with open(fix_filepath, "w") as f:
                print("Max is hand-blackening this file for you with love! <3: " + filename)
                f.write(s)

findreplace()
