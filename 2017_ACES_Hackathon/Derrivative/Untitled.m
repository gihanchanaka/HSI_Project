A= [ 1 2 3 1 1 ; 3 2 1 1 1 ; 1 1 1 1 2 ; 3 1 1 2 1 ]



for i=1:1:5
    X(i)=nnz(A(:,i)==1) ;
end

y=max(X)
cluster1=zeros(y,5)


  for i= 1:5 
      
      
cluster1(:,i)=[find(A(:,i)==1);zeros(y-nnz(find(A(:,i)==1)),1)];
  end
        
      
        
    



 
 
