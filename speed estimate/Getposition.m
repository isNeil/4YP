I = imread('camerapositionfind.png');
imshow(I)
zoom on;
pause() % you can zoom with your mouse and when your image is okay, you press any key
zoom off;
[x,y] = ginput(5)