clear

table_cropped = imread('table_cropped.jpg');


%Inital finding of points on perspective image
% imshow(I);
% [x,y] = getpts;
% save('table_x','x')
% save('table_y','y')


load ( 'table_x1.mat','x' )
load ( 'table_y1.mat','y' )

imshow(table_cropped);
hold on
for i =1:length(x)
    plot(x(i), y(i), 'ro')
end

drawnow
%export_fig('circledtable')

hold off

figure(2);

%0,0 lower left corner, width 402mm, height 402mm
rectangle('Position',[0 0 402 402],'FaceColor',[255/255 229/255 204/255])
rectangle('Position',[7 7 388 388],'FaceColor',[102/255 52/255 0])
axis('off')

graphic_x1= [50,50,100,110,165,230,302,302,352];
graphic_y1= [40,165,262,342,120,232,70,357,190];
hold on
for i =1:length(graphic_x1)
    plot(graphic_x1(i), graphic_y1(i), 'wx')
end

drawnow
coordsreal=[];
for i = 1:length(x)
    coordsreal=[coordsreal [x(i);y(i)]];
end
coordstheory=[];
for i = 1:length(x)
    coordstheory=[coordstheory [graphic_x1(i);graphic_y1(i)]];
end

% %coordsreal
% %coordstheory
% %pyversion
% hemp=fileparts(which('temp.py'));
%     if count(py.sys.path,hemp)==0
%         insert(py.sys.path,int32(0),hemp);
%     end
% py.sys.path
% 
% %H = cv.findHomography(coordsreal, coordstheory)
% 
% %py.temp.opencvtest()
% py.importlib.import_module('cv2')
% py.importlib.import_module('numpy')
% py.temp.homo
% %system('python example.py')