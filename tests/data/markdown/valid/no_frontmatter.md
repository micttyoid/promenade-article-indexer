# Table of Continuous-Time Fourier Transform

## Properties of CT Fourier series

| Property             | Time Domain              | Fourier Domain |
|----------------------|--------------------------|----------------|
| Linearity            | $\alpha x(t)+\beta y(t)$ | $\alpha a_k + \beta b_k$ |
| Translation          | $x(t - t_0)$             | $e^{-jk(2\pi/T)t_0}a_k$ |
| Modulation           | $e^{jM(2\pi/T)t}x(t)$    | $a_{k-M}$ |
| Reflection           | $x(-t)$                  | $a_{-k}$ |
| Conjugation          | $x^*(t)$                 | $a^*_{-k}$ |
| Periodic Convolution | $x \ast y(t)$            | $Ta_kb_k$ |
| Multiplication       | $x(t)y(t)$               | $\displaystyle\sum_{n=-\infty}^{\infty} a_nb_{k-n}$ |

| Property            | |
|---------------------|-| 
| Parseval's relation | $\displaystyle\frac{1}{T}\int_T \|x(t)\|^2 dt = \sum_{k=-\infty}^{\infty} \|a_k\|^2$ |
| Even symmetry | $x$ even $\Leftrightarrow$ $a$ even |
| Odd symmetry  | $x$ odd $\Leftrightarrow$ $a$ odd   |
| Real          | $x$ real $\Leftrightarrow$ $a$ conjugate symmetric |

## Properties of the CT Fourier transform

| Property                   | Time Domain       | Frequency Domain   |
|----------------------------|-------------------|--------------------|
| Linearity                  | $a_1x_1(t) + a_2x_2(t)$ | $a_1X_1(\omega) + a_2X_2(\omega)$ |
| Time-domain shifting       | $x(t - t_0)$            | $e^{-j\omega t_0}X(\omega)$ |
| Frequency-Shifting         | $e^{j\omega_0 t}x(t)$   | $X(\omega - \omega_0)$ |
| Scaling                    | $x(at)$ | $\displaystyle\frac{1}{\|a\|}X\left(\frac{\omega}{a}\right)$ |
| Conjugation                | $x^*(t)$           | $X^*(-\omega)$ |
| Duality                    | $X(t)$             | $2\pi x(-\omega)$ |
| Time-domain convolution    | $x_1(t) * x_2(t)$  | $X_1(\omega)X_2(\omega)$ |
| Time-domain multiplication | $x_1(t)x_2(t)$     | $\displaystyle\frac{1}{2\pi}X_1 * X_2(\omega)$ |
| Time-domain differentiation|$\displaystyle\frac{d}{dt}x(t)$ | $j\omega X(\omega)$ |
|Frequency-domain differentiation|$tx(t)$|$j\frac{d}{d\omega}X(\omega)$|
| Time-domain integration    | $\displaystyle\int_{-\infty}^t x(\tau)d\tau$ | $\displaystyle\frac{1}{j\omega}X(\omega)+\pi X(0)\delta(\omega)$ |

| Property            |                                                 |
|---------------------|-------------------------------------------------|
| Parseval's Relation | $\displaystyle\int_{-\infty}^{\infty} \|x(t)\|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} \|X(\omega)\|^2 d\omega$     |
| Even  | $x(t)$ even $\Leftrightarrow$ $X(\omega)$ even                |
| Odd   | $x(t)$ odd $\Leftrightarrow$ $X(\omega)$ odd                  |
| Real  | $x(t)$ real $\Leftrightarrow$ $X(\omega)$ conjugate symmetric |

## Transform pairs for the CT Fourier transform

|   | $x(t)$            | $X(\omega)$                             |
|---|-------------------|-----------------------------------------|
| 1 | $\delta(t)$       | $1$                                     |
| 2 | $u(t)$            | $\displaystyle\pi\delta(\omega) + \frac{1}{j\omega}$ |
| 3 | $1$               | $2\pi\delta(\omega)$                    |
| 4 | $\text{sgn}(t)$   | $\displaystyle\frac{2}{j\omega}$        |
| 5 | $e^{j\omega_0 t}$ | $2\pi\delta(\omega - \omega_0)$         |
| 6 | $\cos(\omega_0 t)$| $\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$ |
| 7 | $\sin(\omega_0 t)$| $\displaystyle\frac{\pi}{j}[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)]$ |
| 8 | $\text{rect}(\frac{t}{T})$      | $\displaystyle\|T\|\text{sinc}(\frac{T\omega}{2})$ |
| 9 | $\displaystyle\frac{\|B\|}{\pi}\text{sinc}(Bt)$  | $\displaystyle\text{rect}(\frac{\omega}{2B})$ |
| 10| $e^{-at}u(t),\ \text{Re}\lbrace a\rbrace > 0$ | $\displaystyle\frac{1}{a + j\omega}$ |
| 11| $t^{n-1}e^{-at}u(t),\ \text{Re}\lbrace a\rbrace > 0$ | $\displaystyle\frac{(n-1)!}{(a + j\omega)^n}$ |
| 12| $\displaystyle\text{tri}(\frac{t}{T})$ | $\displaystyle\frac{\|T\|}{2}\text{sinc}^2(\frac{T\omega}{4})$ |


## Reference(s)

- M. D. Adams, _Signals and Systems_, 3rd ed. The University of Victoria, Victoria, British Columbia, Canada, 2020.