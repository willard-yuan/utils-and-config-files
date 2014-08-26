clear all; clc;
[a,b,c]= xlsread('2.xlsx'); %读取数据
num=size(c,1);
d={};
for ii=1:num
    if ~isnan(c{ii,1})
        d =[d;c(ii,:)];
    end
end
size_d = size(d,1);
e = zeros(size_d, 2);
for i = 1:size_d
    for j = 1:2
        temp = cell2mat(d(i,j));
        e(i,j) = temp(1,1);
    end
end
xlswrite('test.xlsx',e); %保存数据
