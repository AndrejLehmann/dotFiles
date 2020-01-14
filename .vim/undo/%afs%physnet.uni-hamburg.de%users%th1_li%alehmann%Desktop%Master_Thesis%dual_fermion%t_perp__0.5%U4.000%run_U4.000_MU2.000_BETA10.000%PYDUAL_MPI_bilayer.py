Vim�UnDo� .���q����h�����d��Y`�/��;r����  A   }  'mesh_file'                       : '../../kmesh_irreducible_wedge_2d.h5',                 #file for the irreducible k-mesh   �   '                       Yo�5    _�                            ����                                                                                                                                                                                                                                                                                                                                                             Yo��    �        z      import dual_mpi5�_�                  e       ����                                                                                                                                                                                                                                                                                                                                                             Yo�     �  d  f  z      )    parms["MU"]=dual_mpi.run(hmlt, parms)5�_�                   e       ����                                                                                                                                                                                                                                                                                                                                                             Yo�     �  d  f  z      (    parms["MU"]=dual_pi.run(hmlt, parms)5�_�                   e       ����                                                                                                                                                                                                                                                                                                                                                             Yo�     �  d  f  z      '    parms["MU"]=dual_i.run(hmlt, parms)5�_�                   e       ����                                                                                                                                                                                                                                                                                                                                                             Yo�    �  d  f  z      &    parms["MU"]=dual_.run(hmlt, parms)5�_�                   ,       ����                                                                                                                                                                                                                                                                                                                           d         ,          v       Yo��     �  +  -  z   9   /  #write a copy of the parameters for reference   4  write_parameter_file(runfilename, parms, mpi.rank)   :  write_parameter_file(runfilename+'.h5', parms, mpi.rank)       �  #if this is a full calculation generate the initial guess; for a single_shot calculation, we read the hybridization present in this directory   "  if it==0 and single_shot==False:       if load_previous==False:   e      dual.run(hmlt, parms, 'initialguess') #must be executed in parallel, otherwise threads get lost   i      convert_Delta_to_F('Delta_tau00.h5', parms["F"], parms["FLAVORS"], parms["PARAMAGNETIC"], mpi.rank)   @      file_backup(DMFTfilelist, label='_initial', rank=mpi.rank)   	    else:         if mpi.rank==0:   7        print "copying hybridization from previous run"   .        shutil.copy("../%s"%(parms["F"]), ".")   1        shutil.copy("../%s"%("Delta_00.h5"), ".")   B        #all other input files to dual are generated by the solver     #end it==0         if mpi.rank==0:   I    shutil.copy("Delta_00.h5", "Delta_old.h5") #Delta_old is read by dual         if(parms["solver"]=='cthyb'):       cthyb.solve(parms)   O    cthyb.evaluate(parms, 'hr') #evaluate the results (uses MPI for the vertex)      elif(parms["solver"]=='diag'):   p    get_ed_parameters('Delta.h5',parms["V_VECTOR"],parms["E_VECTOR"],nparams=parms["N_bathsites"],rank=mpi.rank)       diag.solve(parms, 'hr')       #  #calculate Green function moments   ]  #NOTE: these moments are only valid for DMFT calculations, where the density of the lattice   a  #coincides with the density of the impurity problem (at least when self-consistency is reached)   ,  if dmft and not parms["solver"] == 'diag':   v    get_moments(parms["U_MATRIX"], parms["EPSILOND_VECTOR"], parms["density"], parms["MOMENTS_H"], parms["MOMENTS_G"],   V                parms["MOMENTS_F"], parms["FLAVORS"], parms["PARAMAGNETIC"], mpi.rank)       3  #convert data from the evaluator to the DF format   w  if not parms["solver"] == 'diag': convert_solver_gt(parms["gtau"], parms["FLAVORS"], parms["PARAMAGNETIC"], mpi.rank)     if(parms["MEASURE_gw"]):   U    convert_solver_gw(parms["gw"], parms["FLAVORS"], parms["PARAMAGNETIC"], mpi.rank)       if(parms["MEASURE_fw"]):   Z      convert_solver_gw(parms["sigma"], parms["FLAVORS"], parms["PARAMAGNETIC"], mpi.rank)         #do selfconsistency   
  if dmft:       mpi.world.barrier()       if mpi.rank==0:   ,     shutil.copy("gt.h5","gt"+str(it)+".h5")   .     shutil.copy("gt.dat","gt"+str(it)+".dat")   -    parms["MU"]=dual.run(hmlt, parms, 'DMFT')     else:   A    #make backup copy of all DF input files for the 2nd order run   (    if mpi.rank==0 and df_iterations==1:         dir = "2nd_order_run"   .      if not os.path.isdir(dir): os.mkdir(dir)   9      files = BACKUPfilelist+glob.glob("gammaw.part*.h5")   0      file_backup(files, rank=mpi.rank, dir=dir)       #end mpi.rank==05�_�      	             ,       ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo��     �  +  ,            5�_�      
           	   *   &    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo��     �   )   +  A      dload_previous                       = False                #whether to load F(tau) from previous run5�_�   	              
   *   )    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo��     �   )   +  A      dload_previous                       = Truee                #whether to load F(tau) from previous run5�_�   
                 +   &    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo��     �   *   ,  A      fdmft_iterations                     = 15                             #maximum number of DMFT iteration5�_�                    +   &    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo��     �   *   ,  A      edmft_iterations                     = 5                             #maximum number of DMFT iteration5�_�                    �   '    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�     �   �   �  A      }  'mesh_file'                       : '../../kmesh_irreducible_wedge_2d.h5',                 #file for the irreducible k-mesh5�_�                    �   '    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�'     �   �   �  A      w  'mesh_file'                       : 'kmesh_irreducible_wedge_2d.h5',                 #file for the irreducible k-mesh�   �   �  A    5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�1     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',                 #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�1     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',                #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�1     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',               #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�2     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',              #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�2     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',             #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�2     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',            #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�2     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',           #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�2     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',          #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�2     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',         #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�3     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',        #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�3     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',       #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�3     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',      #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�3     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',     #file for the irreducible k-mesh5�_�                    �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�3     �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',    #file for the irreducible k-mesh5�_�                     �   �    ����                                                                                                                                                                                                                                                                                                                           ,         ,          v       Yo�4    �   �   �  A      �  'mesh_file'                       : '/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5',   #file for the irreducible k-mesh5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Yo��     �        z    �        z      �import dual_sta# /afs/physnet.uni-hamburg.de/users/th1_li/alehmann/Desktop/Master_Thesis/dual_fermion/kmesh_irreducible_wedge_2d.h5't5��