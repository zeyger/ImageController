#!/usr/bin/env bash
th neural_style.lua -style_image input/style.jpg -content_image input/image.jpg -output_image output/output.png -gpu -1 -print_iter 1 -num_iterations 101 -image_size 16

