Vim�UnDo� ��V�7���)cX)!�eĨ�F��>�$ķ��6�   >       =          )       )   )   )    ]���    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ]���     �                wn = 05�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]���    �                    if(i.find('wn=')!=-1):         wn_ = i.partition('=')[2]         wn  = int(wn_)         print "wn = %s"%(wn)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ]���    �         7      #mesh_file = "../../kmesh_gxm_3d.h5"5�_�                    %        ����                                                                                                                                                                                                                                                                                                                            !           %           V        ]��	     �   %   +   7    �   %   &   7    5�_�                    &       ����                                                                                                                                                                                                                                                                                                                            !           %           V        ]��     �   %   '   <      if file_name == "":5�_�                    &       ����    &                                                                                              &                                                                                                                                                                                                                      !           %           V        ]��    �   %   '   <      if name == "":5�_�                    '       ����    &                                                                                              &                                                                                                                                                                                                                      !           %           V        ]��     �   &   (   <      ;  print "  file as argument is needed. Provide by file=..."5�_�      	              '       ����    &                                                                                              '                                                                                                                                                                                                                      !           %           V        ]��    �   &   (   <      7  print "   as argument is needed. Provide by file=..."5�_�      
           	   '   2    ����    &                                                                                              '                                                                                                                                                                                                                      !           %           V        ]��      �   &   (   <      ;  print "  mesh as argument is needed. Provide by file=..."5�_�   	              
   '   2    ����    &                                                                                              '                                                                                                                                                                                                                      !           %           V        ]��"    �   &   (   <      7  print "  mesh as argument is needed. Provide by =..."5�_�   
                 *   	    ����    &                                                                                              '                                                                                                                                                                                                                      !           %           V        ]��)     �   )   +   <        print "file = %s"%(file_name)5�_�                    *   	    ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   !           %           V        ]��,    �   )   +   <        print " = %s"%(file_name)5�_�                    /       ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   !           %           V        ]��5     �   .   0   <      &gxm_path.load("../../kmesh_gxm_3d.h5")5�_�                    /       ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   !           %           V        ]��7     �   .   0   <      gxm_path.load("")5�_�                    /       ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   !           %           V        ]��8    �   .   0   <      gxm_path.load(")5�_�                    2       ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   !           %           V        ]��J     �   1   3   <      outfile += '_wn%i.dat'%(wn)5�_�                    2       ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   !           %           V        ]��J     �   1   3   <      outfile += '_n%i.dat'%(wn)5�_�                    2       ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   !           %           V        ]��J     �   1   3   <      outfile += '_%i.dat'%(wn)5�_�                    2       ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   !           %           V        ]��K     �   1   3   <      outfile += '_i.dat'%(wn)5�_�                    2       ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   !           %           V        ]��L     �   1   3   <      outfile += '_.dat'%(wn)5�_�                    2       ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   !           %           V        ]��O    �   1   3   <      outfile += '.dat'%(wn)5�_�                    4        ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   !           %           V        ]��g   	 �   3   4          f.write("# wn = %i\n"%(wn))5�_�                    4   /    ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   4   "       4   /       v   /    ]��t     �   3   5   ;      hf.write("#   k_[0]   |    k_[1]   |   k_[2]    |   Re j=0   |    Im j=0   |   Re j=1   |    Im j=1  \n")�   4   5   ;    5�_�                    4   <    ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   4   "       4   /       v   /    ]��u     �   3   5   ;      vf.write("#   k_[0]   |    k_[1]   |   k_[2]    |   k_[2]    ||   Re j=0   |    Im j=0   |   Re j=1   |    Im j=1  \n")5�_�                    4   3    ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   4   "       4   /       v   /    ]��x   
 �   3   5   ;      uf.write("#   k_[0]   |    k_[1]   |   k_[2]    |   k_[2]    |   Re j=0   |    Im j=0   |   Re j=1   |    Im j=1  \n")5�_�                    4   4    ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   4   "       4   /       v   /    ]��~     �   3   5   ;      uf.write("#   k_[0]   |    k_[1]   |   k_[2]    |    wn      |   Re j=0   |    Im j=0   |   Re j=1   |    Im j=1  \n")5�_�                    4   7    ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   4   "       4   /       v   /    ]��    �   3   5   ;      vf.write("#   k_[0]   |    k_[1]   |   k_[2]    |     wn      |   Re j=0   |    Im j=0   |   Re j=1   |    Im j=1  \n")5�_�                    :   6    ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   4   "       4   /       v   /    ]���    �   9   ;   ;      �    f.write("%.10f %.10f %.10f %.10f %.10f %.10f %.10f\n"%(k_[0], k_[1], k_[2], value_j0.real, value_j0.imag, value_j1.real, value_j1.imag))5�_�                    :   V    ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   4   "       4   /       v   /    ]���    �   9   ;   ;      �    f.write("%.10f %.10f %.10f %.10f %.10f %.10f %.10f %.10f\n"%(k_[0], k_[1], k_[2], value_j0.real, value_j0.imag, value_j1.real, value_j1.imag))5�_�                    5        ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   5           :                   ]���     �   5   ;   ;          k_ = gxm_path.vector(k)   -    value_j0=p.value(0, wn, k[0], k[1], k[2])   -    value_j1=p.value(1, wn, k[0], k[1], k[2])   Z    #f.write("%.10f %.10f %.10f %.10f %.10f\n"%(k[0], k[1], k[2], value.real, value.imag))   �    f.write("%.10f %.10f %.10f %.10f %.10f %.10f %.10f %.10f\n"%(k_[0], k_[1], k_[2], wn, value_j0.real, value_j0.imag, value_j1.real, value_j1.imag))�   4   6   ;      'for n,k in enumerate(gxm_path.kpoints):5�_�                     5        ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   5           :                   ]���     �   4   6   ;    5�_�      !               5        ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   6           ;                   ]���     �   4   6   <       5�_�       "           !   5       ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   6           ;                   ]���     �   4   6   <      for wn in range()5�_�   !   #           "   5       ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   6           ;                   ]���    �   4   6   <      for wn in range(N_w)5�_�   "   $           #          ����    &                                              *   	                                           *   	                                                                                                                                                                                                                   6           ;                   ]���     �         <    �         <    5�_�   #   %           $          ����    '                                              +   	                                           +   	                                                                                                                                                                                                                   7           <                   ]���     �         =      Ny = parms["N_y"]5�_�   $   &           %          ����    '                                              +   	                                           +   	                                                                                                                                                                                                                   7           <                   ]���    �         =      N_w = parms["N_y"]5�_�   %   '           &   <       ����    '                                              +   	                                           +   	                                                                                                                                                                                                                   7           <                   ]���     �   <   >   =    5�_�   &   (           '   =        ����    '                                              +   	                                           +   	                                                                                                                                                                                                                   7           <                   ]���     �   <   >   >       5�_�   '   )           (   =       ����    '                                              +   	                                           +   	                                                                                                                                                                                                                   7           <                   ]���     �   <   >   >          f.write()5�_�   (               )   =       ����    '                                              +   	                                           +   	                                                                                                                                                                                                                   7           <                   ]���    �   <   >   >          f.write("")5��