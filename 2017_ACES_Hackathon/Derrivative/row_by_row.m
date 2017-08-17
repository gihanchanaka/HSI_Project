clear all;
close all;
clc;

for_cov = create_datamat(5627,5803); %%use this if need to create the 2D mat with rows as pixels and cols as spectral data
 
for_covN = for_cov/708.640605857058^(0.5);
covariance=cov(for_covN); 
%after finding the # of pc
[ei_vec, ei_val]=eigs(covariance,7);

transform=ei_vec';
   
%pixels in transformed 7 dim space
px_new=transform*(for_cov)';

scatter3(px_new(1,:),px_new(3,:),px_new(6,:));
figure;
scatter3(for_cov(:,10),for_cov(:,20),for_cov(:,30));



% set_1 = px_new(:,104:104+261);
% % to find the best sigma for mode 3
% 
% eigen_gap=zeros(12,40);
% for k=1:40;
%     sigma(k)=k/40;
%     for i=1:262
%         for j=1:262
%             disp(i,j) = norm(set_1(:,i)-set_1(:,j));
%         end
%     end
%     dispN = disp/max(max(disp));
%     aff1 = exp((-dispN.^2)/(2*sigma(k)^2));
%     D = diag((sum(aff1,2).^(-0.5)));
%     L = D*aff1*D;
%     %[ei_vec_lap,ei_val_lap]=eigs(L,dom_eigvalues);
%     dom_eigvalues=13;
%     ei_val_lap=eigs(L,dom_eigvalues);
%     eigen_gap(:,k)=abs(diff(ei_val_lap));
%     [dominant_mode(k),index(k)]=max(eigen_gap(:,k));
% end
% 
% stem(sigma,index)
% title('dominant mode at different sigma values');
% xlabel('sigma');
% ylabel('dominant mode');
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  
%  sigma=4/40;
% for i=1:262
%     for j=1:262
%         disp(i,j) = norm(set_1(:,i)-set_1(:,j));
%     end
% end
% dispN = disp/max(max(disp));
% aff1 = exp((-dispN.^2)/(2*sigma^2));
% D = diag((sum(aff1,2).^(-0.5)));
% L = D*aff1*D;
% dom_eigvalues=3;
% [ei_vec_lap,ei_val_lap]=eigs(L,dom_eigvalues);
%   
% for lll=1:dom_eigvalues
%     if ei_vec_lap(1,lll)<0
%         ei_vec_lap(:,lll)=ei_vec_lap(:,lll)*(-1);
%     else
%         ei_vec_lap(:,lll)=ei_vec_lap(:,lll);
%     end
% end
% 
% idx_5632=kmeans(ei_vec_lap,3);
% 
% 
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% a1=find(idx_5632==1);
% for i=1:length(a1)
%     b1(i,:)=for_cov(a1(i),:);
% end
% b1_mean=sum(b1)/length(a1);
% 
% a2=find(idx_5632==2);
% for i=1:length(a2)
%     b2(i,:)=for_cov(a2(i),:);
% end
%  b2_mean=sum(b2)/length(a2);
% 
%  
%  a3=find(idx_5632==3);
% for i=1:length(a3)
%     b3(i,:)=for_cov(a3(i),:);
% end
% b3_mean=sum(b3)/length(a3);
% 
% % plot(b1_mean,'b');
% % hold on;
% % plot(b2_mean,'k');
% % plot(b3_mean,'r');
% % hold off;
% 
% scatter3(ei_vec_lap(:,1),ei_vec_lap(:,2),ei_vec_lap(:,3));


















