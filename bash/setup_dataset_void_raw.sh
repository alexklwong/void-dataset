#!/bin/bash

mkdir -p 'data'
mkdir -p 'void_raw'
mkdir -p 'void_raw/tmp'

cd 'void_raw'

void_raw_urls=(

https://drive.google.com/uc?id=1DRgnghQfBZ7tZ4C7ncIkgxyor6d4Ogbf
https://drive.google.com/uc?id=1aY1MCa4ipZ5Y_MVt4JmgvXcklWdUXMfR
https://drive.google.com/uc?id=1pexjlAU77jtRPfgIqFDntQ09Cewcjlel
https://drive.google.com/uc?id=1H-TyPxhi0hloOcp-QOQda_Y9Let-A59Z
https://drive.google.com/uc?id=1u36lDAvPenkVKXBidHscn0be8Cqt6tyL
https://drive.google.com/uc?id=1Z3QwgJUzw6UsGIJd26584z60StL7Iv5D
https://drive.google.com/uc?id=1Rq_Xxof8h9yIj8VagdSxiKLOOC7ZAOCp
https://drive.google.com/uc?id=1q5O8MgvzgayjvokMx1Tg_aEw7Ts_F_Uz
https://drive.google.com/uc?id=1O6AcOzPi-buiwbzZ0wXaZfTVDsMHnKtI
https://drive.google.com/uc?id=1gNCxl2pHaN7qQf13U-Y0Ka7StcBOxACo
https://drive.google.com/uc?id=1X6wdH9EkQ4y9EyNc5x6exeQa_us_4JAH
https://drive.google.com/uc?id=1QYIT1dCeBZZGmh09PYNX5_9gpWgG3gGu
https://drive.google.com/uc?id=1vZ4Aszgf8JMBXluQS-LBFF49thYnRwuS
https://drive.google.com/uc?id=1-o-Bcah9bt-oebq-orTAppJp2MDTpxly
https://drive.google.com/uc?id=1CYiWP32wC5x8pi9j3jbuFV0GMXX_RVrk
https://drive.google.com/uc?id=1DUO1BtT4PDxRJjqL0czSkCykqU40eYti
https://drive.google.com/uc?id=1tuiPFwOuh9fQatCk4KIQRtutLY7bzKw-
https://drive.google.com/uc?id=10OAPZmisLz-hDp1Hg3AEOJnMZHwm1k5C
https://drive.google.com/uc?id=1x4S5BiZglFd-UsBru2JnDrpO9NZlXzyE
https://drive.google.com/uc?id=18KBwQLd6R--Tx6wpaC80ftTTOLMcUAoE
https://drive.google.com/uc?id=1jv2PnzIzoM-OS4UaaEPFLbm8xCtdpVQC
https://drive.google.com/uc?id=1qI_5XCAMH3rEpFpI2QJqyhNjpHbC0IzE
https://drive.google.com/uc?id=1FeOyyUlnEj9xWdl63VAgd-IK5b7EwRlC
https://drive.google.com/uc?id=1UTxXeC13ZTGW3vgRX0i3exwxszqoHxpI
https://drive.google.com/uc?id=19g2gGjr3d3py27TbPQot4dK4ExUXLmuw
https://drive.google.com/uc?id=1VJx91tc9gCH1KKHidbCvGGs8sR9V-bJe
https://drive.google.com/uc?id=18h4nqRUBHUcBvr34ArKF6ehcBPfHDQEB
https://drive.google.com/uc?id=1h4gw385JGwzflnXp13A04NVj2bW0kZQT
https://drive.google.com/uc?id=1ubrXyael_v_UqdTduH5EpOTGRmIelvng
https://drive.google.com/uc?id=1tuCsOOUtTWoPADiKxf5tiFLmNpHCmdyL
https://drive.google.com/uc?id=1nSl7L5ur6dv8-l_bJe-ICAOpvJSR1DDD
https://drive.google.com/uc?id=1VZRh8R6M98vD1Uf4feEoG1qL7abiJsyL
https://drive.google.com/uc?id=1HGiRatJc2aYpTm6krVheYHBQrMr_MqiG
https://drive.google.com/uc?id=1KxcwHlgF_VpWMMdN2ktugIifapvyrYZ6
https://drive.google.com/uc?id=1ryrTL4QnYiPWP60CiT4FanyW8KfoqsaF
https://drive.google.com/uc?id=1Dh8Cf0SuW1kcuMl15GfQQ9aBoGEwi9Vq
https://drive.google.com/uc?id=1Qv8cOShMjHuqc5lFiiW7Sv2newCHof_v
https://drive.google.com/uc?id=1iJvQ0esgqNORxC8uGDC4iGS-ro7GXYGK
https://drive.google.com/uc?id=16aqdQX2Vr7MWCi-YGnI9d2-LpcqGDCyP
https://drive.google.com/uc?id=1otVDlZRPKJjD9C4whd3zEZclXi_KhZ5-
https://drive.google.com/uc?id=1Yq3NYxUHc7N2TwYBxxmsgJQZPkC44DZ3
https://drive.google.com/uc?id=1dkixsIX59AH7Xv6eBmhfwfGJG2EnpRUv
https://drive.google.com/uc?id=1_lG8AUbBwDI89SMdygmddJpmbnrxz2Bw
https://drive.google.com/uc?id=1luv30G1rgKnUk05k0-mSNWQRzIs8al8o
https://drive.google.com/uc?id=1uqrLY4yCEOar_oDSVIJu12L3wHMNOkiS
https://drive.google.com/uc?id=1QANavSjPsDnE1uhueXFI8AKk9Q1RGHw7
https://drive.google.com/uc?id=1rS97bb9w8iA7sXQXZvziTeDYC1QptXtq
https://drive.google.com/uc?id=1dNGftbXtkzZtREjlm_lQHijTdfFvRBWN
https://drive.google.com/uc?id=11PLDZ59byye3VrMkvM_0mICln-Le-JIF
https://drive.google.com/uc?id=1zvKGB1qRVqV_knC2k47kEytskqVbvj14
https://drive.google.com/uc?id=1kOtWKDHxEROdEwfd9DOb7mSxvaT48vRS
https://drive.google.com/uc?id=1KVbmyIUDIwZARSrfFvN6Y33gzUAU6ILp
https://drive.google.com/uc?id=1ON-fJp2lL74o42lOVGuL1VqFSEn5wfhB
https://drive.google.com/uc?id=1DICJXD_Eu6wdB8kh5QvJX02xUdsUTKbD
https://drive.google.com/uc?id=1lQeQ3r-1Q4w7tVU_l7XX_37xjrK55RLx
https://drive.google.com/uc?id=1JvOd_y3a33UKTK_9pZ0jHo3AvXDGxnoY
)

if [ $# -eq 0 ]; then
  for file_url in ${void_raw_urls[@]}; do
    gdown $file_url
  done
fi

file_id=1
while [ $file_id -le ${#void_raw_urls[@]} ]; do
  unzip -o 'void_raw-'${file_id}'.zip'
  mv 'void_raw-'${file_id}'.zip' 'tmp/'
  file_id=$(( ${file_id} + 1 ))
done

cd ..
mv void_raw data/void_raw
