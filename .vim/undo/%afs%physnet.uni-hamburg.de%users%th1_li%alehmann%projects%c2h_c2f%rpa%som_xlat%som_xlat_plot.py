Vim�UnDo� ��%j&ӻg8l�F��o�ڬV���C}��C�                                     ]��    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ]�(�    �                   5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�)    �               "ar = HDFArchive('results.h5', 'r')5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             ]�)#     �   	            Soplot(ar['chi_iw'][0,0],     mode='R', linewidth=0.8, label="$\chi_0(i\\omega_n)$")5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             ]�)$     �   	            Roplot(ar['chi_iw'][00],     mode='R', linewidth=0.8, label="$\chi_0(i\\omega_n)$")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�)&     �   
            `oplot(ar['chi_rec_iw'][0,0], mode='R', linewidth=0.8, label="$\chi_\mathrm{0,rec}(i\\omega_n)$")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�)'     �   
            _oplot(ar['chi_rec_iw'][00], mode='R', linewidth=0.8, label="$\chi_\mathrm{0,rec}(i\\omega_n)$")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�)(    �                Soplot(ar['chi_iw'][1,1],     mode='R', linewidth=0.8, label="$\chi_1(i\\omega_n)$")   `oplot(ar['chi_rec_iw'][1,1], mode='R', linewidth=0.8, label="$\chi_\mathrm{1,rec}(i\\omega_n)$")5�_�      	              
       ����                                                                                                                                                                                                                                                                                                                                                             ]�)b    �   	            Qoplot(ar['chi_iw'][0],     mode='R', linewidth=0.8, label="$\chi_0(i\\omega_n)$")5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             ]�)o     �   
            ^oplot(ar['chi_rec_iw'][0], mode='R', linewidth=0.8, label="$\chi_\mathrm{0,rec}(i\\omega_n)$")5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             ]�)x    �   
            coplot(ar['chi_rec_iw_rec0'][0], mode='R', linewidth=0.8, label="$\chi_\mathrm{0,rec}(i\\omega_n)$")5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                             ]�9    �                from pytriqs.gf.local import *5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�?)    �                #from pytriqs.gf.local import *5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             ]�?L   	 �   	            Uoplot(ar['chi_iw_in0'][0],     mode='R', linewidth=0.8, label="$\chi_0(i\\omega_n)$")5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�@�     �                  �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�A     �                 plt.savefig()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�A   
 �                 plt.savefig('')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�J�    �              �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�L�     �                 plt.savefig('chi_iw_nk0.png')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�L�    �                 plt.savefig('chi_iw_k0.png')5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             ]�P�     �   	            !ar = HDFArchive('xlat_E.h5', 'r')5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             ]�P�    �   	            !ar = HDFArchive('xlat_E.h5', 'r')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�Q`    �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�SW     �                Ysys.path.append("/opt/sw/ipython/5.1.0/lib/python2.7/site-packages")  # enthaelt h5py lib5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�SX    �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]��     �                 �              5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             ]��    �                 5��