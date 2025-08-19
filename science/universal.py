from math import pi, sqrt
#                                     Quantity                                 Unit            Value                        u_r(Relative std. uncert.)

c = 299792458                         # speed of light in vacuum               m/s             -                            exact
h_Js = 6.62607015e-34                 # Planck constant                        J*s             -                            exact
h_eVs = h_Js / ...                    # Planck constant                        eV*s            4.135667696e-15              exact                           TODO ...를 기본 전하량(e)로 바꾸기
h_bar_Js = h_Js / ( 2 * pi )          # reduced Planck constant                J*s             1.054571817e-34              exact                           TODO pi를 파이값으로 바꾸기
h_bar_eVs = h_bar_Js / ...            # reduced Planck constant                eV*s            6.582119569e-16              exact                           TODO ...를 기본 전하량(e)로 바꾸기
mu0 = 1.25663706127e-6                # vacuum magnetic permeability           N/A,            1.25663706127(20)e-6         1.6e-10                         TODO 미세구조상수 쓴 식으로 바꾸기
etha0 = 1 / ( mu0 * c * c )           # vacuum electric permittivity           F/m,            8.8541878188(14)e-12         1.6e-10
Z0 = mu0 * c                          # characteristic impedance of vacuum     ohm,            376.730313412(59)            1.6e-10
G = 6.67430e-11                       # Newtonian constant of gravitation      m**3/kg,        6.67430(15)e-11              2.2e-5
m_P = sqrt(h_bar_Js * c / G)          # Planck mass                            kg              2.176434(24)e-8              1.1e-5
T_P = sqrt(h_bar_Js ** 5 / G) / ...   # Planck temperature                     K               1.416784(16)e32              1.1e-5                          TODO ...를 볼츠만 상수(k_B)로 바꾸기
l_P = h_bar_Js / ( m_P * c )          # Planck length                          m               1.616255(18)e-35             1.1e-5
t_P = l_P / c                         # Planck time                            s               5.391247(60)e-44             1.1e-5