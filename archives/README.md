
# acoustic_radio 

This is a repository for my research on digital acoustic communication. 
* GNURadio
* Python
* C++

## 2019-9-12
1. Notes.

- Made some changes on the flowgraph, shrinked the payload size(20 to 2) in packet encoder block. Which seems like the reason behind lossing characters in text files. 
- We are now have no problem transmitting small size files. (We tested 46.9kb jpg)
- We learned that /build could be in our way when we try to rebulid our OutOfTree blocks.
- Simulaton looks like is working properly now. 

2. What's next
* Move forward and use laptop speaker&microphone to transmit qpsk signals. 

## 2019-6-7
1. Notes.

- Using QPSK transmitting a image over the simulated channal works in **mpsk_stage6_mod2.grc**
- Sometimes the image got cutoff, possibally because of the absence of error correction, will be added in the next update

2. What's next
* Add error corection.
