Vim�UnDo� Mܭ�7	���" �{�*_Gw�������|�?   %   "      printf ("%s\n", strings[i]);                             \|�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             \|�    �                   5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             \|�     �   	      %            size_t size;5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \|�     �   
      %              char **strings;5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \|�     �         %                size_t i;5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \|�     �         %      )            size = backtrace (array, 10);5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \|�     �         %      8              strings = backtrace_symbols (array, size);5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \|�     �         %      >                printf ("Obtained %zd stack frames.\n", size);5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             \|�     �         %      ,                  for (i = 0; i < size; i++)5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             \|�     �         %      5                         printf ("%s\n", strings[i]);5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             \|�     �         %      #                    free (strings);5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             \|�    �         %      "      printf ("%s\n", strings[i]);5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \|�    �         %      #       printf ("%s\n", strings[i]);5��