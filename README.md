# DotFiles
My config files

<h3 align="center"><img src="data/icons/64/com.github.artemanufrij.trimdown.svg"/><br>

If you are looking to get the same setup as mine you can do so by following those step

**Dependencies**

```
Sudo pacman -S git stow bspwm sxhkd i3-gaps rofi polybar light yay
```

**then do**

```
yay -S ttf-font-awesome nerd-fonts-source-code-pro i3lock-fancy-git
```

You'll also need [Ant-Dracula theme](https://github.com/EliverLara/Ant-Dracula) , [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)  ,
zsh dracula theme and [Powerline-Shell](https://github.com/b-ryan/powerline-shell) 

**after you do so, clone the repository**

```
cd ~/
git clone https://github.com/ronniedroid/DotFiles.git
cd DotFiles
stow (name of the folder of the thing you want to use)
```

for example

```
stow i3
stow polybar
stow home
```

and so on...


Note, this instaraction is for Arch-bases linux only, you can replucate this setup on other distros too, all you ahve to do is install the dependenies then follow the instarctions
