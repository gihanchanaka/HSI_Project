%clear all;
%close all;
%clc;

 plot(soil(:,2),'k');
hold on;
plot(vegetation(:,2),'b');
plot(water(:,2),'r');
hold off

%for_cov = create_datamat(5627,5803); %%use this if need to create the 2D mat with rows as pixels and cols as spectral data

% for_covN = for_cov/(708.640605857058^(0.5));
% for i=1:100
%     %plot(for_cov(i*100,:))
%     hold on;
% end
%%%covariance=cov(for_covN); 
%after finding the # of pc
%%%[ei_vec, ei_val]=eigs(covariance,7);
% stem(log(abs((diff(diag(ei_val))))));
% title('logarithmic differences between adjacent eigen values');
% xlabel('index of eigen value');
% ylabel('log of eigen value difference');
% % 
%transformation matrix
%%%transform=ei_vec';
   
%pixels in transformed 7 dim space
%%%px_new=transform*(for_covN)';
%%%%%%%%%%%%%%%%%%%%%%%%%
% % % select=px_new';
% % % idx_test=kmeans(select,3);
% % % 
% % % a1=find(idx_test==1);
% % % for i=1:length(a1)
% % %     b1(i,:)=for_cov(a1(i),:);
% % % end
% % % b1_mean=sum(b1)/length(a1);
% % % 
% % % a2=find(idx_test==2);
% % % for i=1:length(a2)
% % %     b2(i,:)=for_cov(a2(i),:);
% % % end
% % %  b2_mean=sum(b2)/length(a2);
% % % 
% % %  
% % %  a3=find(idx_test==3);
% % % for i=1:length(a3)
% % %     b3(i,:)=for_cov(a3(i),:);
% % % end
% % % b3_mean=sum(b3)/length(a3);
% % % 
% % % plot(b1_mean,'b');
% % % hold on;
% % % plot(b2_mean,'k');
% % % plot(b3_mean,'r');
% % % hold off;
