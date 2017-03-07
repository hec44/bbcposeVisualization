%Beta function, write a csv with information of shortbbcpose dataset
%By: Hec44

function  struct2csv(structfile,csvPath)
  struct=load([structfile]).shortbbcpose;
  for index=[1 2 3 4 5]
    frames=struct(index).train_frames %get frames names
    frames=transpose(frames)
    %concatenate squeeze and transpose joints for csv format
    joints=[struct(index).train_joints(1,:,:),struct(index).train_joints(2,:,:)]
    joints=squeeze(joints)
    joints=transpose(joints)
    %finally concatenate information and write csv
    csvInfo=[frames,joints]
    csvwrite(strcat(csvPath,'/',num2str(index),'.csv'),csvInfo)
  end
endfunction
