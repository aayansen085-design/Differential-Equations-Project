# ================================================================
# DIFFERENTIAL EQUATIONS TOOLKIT
# ODE + PDE SOLVER FOR MATHEMATICS STUDENTS
# ================================================================

import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------

st.set_page_config(
    page_title="Differential Equations Toolkit",
    page_icon="∂",
    layout="wide"
)

# ------------------------------------------------
# SYMBOLS
# ------------------------------------------------

x, y, z, t = sp.symbols("x y z t")
p, q = sp.symbols("p q")

# ------------------------------------------------
# TITLE
# ------------------------------------------------

st.title("∂ Differential Equations Toolkit")
st.subheader("Ordinary and Partial Differential Equations")

st.write(
    """
    This project is designed for mathematics students to study,
    solve and visualize Ordinary Differential Equations (ODEs)
    and Partial Differential Equations (PDEs).
    """
)

# ------------------------------------------------
# SIDEBAR MENU
# ------------------------------------------------

topic = st.sidebar.selectbox(
    "Select Topic",
    [
        "Introduction",
        "First Order ODE",
        "Linear ODE",
        "Bernoulli Equation",
        "Euler Numerical Method",
        "Runge-Kutta Method",
        "Introduction to PDE",
        "Lagrange PDE",
        "Charpit PDE",
        "Linear PDE",
        "Non-Linear PDE",
        "About Project"
    ]
)

# ================================================================
# INTRODUCTION
# ================================================================

if topic == "Introduction":

    st.header("1. Introduction to Differential Equations")

    st.write(
        """
        A differential equation is an equation involving an unknown
        function and one or more of its derivatives.
        """
    )

    st.latex(r"""
    F(x,y,y',y'',\ldots)=0
    """)

    st.write("Differential equations are mainly divided into:")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            """
            ### Ordinary Differential Equation (ODE)

            An ODE contains derivatives with respect to one
            independent variable.

            Example:
            """
        )

        st.latex(r"""
        \frac{dy}{dx}+y=x
        """)

    with col2:
        st.success(
            """
            ### Partial Differential Equation (PDE)

            A PDE contains partial derivatives with respect
            to two or more independent variables.

            Example:
            """
        )

        st.latex(r"""
        \frac{\partial z}{\partial x}
        +
        \frac{\partial z}{\partial y}=0
        """)

    st.header("Order of a Differential Equation")

    st.write(
        """
        The order of a differential equation is the order of the
        highest derivative occurring in the equation.
        """
    )

    st.latex(r"""
    \frac{dy}{dx}+y=0
    """)

    st.write("This is a first-order differential equation.")

    st.latex(r"""
    \frac{d^2y}{dx^2}+3\frac{dy}{dx}+2y=0
    """)

    st.write("This is a second-order differential equation.")


# ================================================================
# FIRST ORDER ODE
# ================================================================

elif topic == "First Order ODE":

    st.header("2. First Order Ordinary Differential Equation")

    st.write(
        """
        A first-order ODE contains the first derivative of the
        dependent variable.
        """
    )

    st.latex(r"""
    \frac{dy}{dx}=f(x,y)
    """)

    st.subheader("Method of Separation of Variables")

    st.latex(r"""
    \frac{dy}{dx}=f(x)g(y)
    """)

    st.latex(r"""
    \frac{dy}{g(y)}=f(x)\,dx
    """)

    st.latex(r"""
    \int\frac{dy}{g(y)}
    =
    \int f(x)\,dx+C
    """)

    st.subheader("Example")

    st.latex(r"""
    \frac{dy}{dx}=xy
    """)

    st.latex(r"""
    \frac{dy}{y}=x\,dx
    """)

    st.latex(r"""
    \ln|y|=\frac{x^2}{2}+C
    """)

    st.latex(r"""
    y=Ce^{x^2/2}
    """)

    st.divider()

    st.subheader("Solve a separable equation")

    equation = st.text_input(
        "Enter f(x,y) for dy/dx = f(x,y)",
        "x*y"
    )

    if st.button("Solve ODE"):

        try:

            f = sp.sympify(equation)

            solution = sp.dsolve(
                sp.Eq(
                    sp.diff(sp.Function("y")(x), x),
                    f.subs(y, sp.Function("y")(x))
                )
            )

            st.success("Solution:")

            st.latex(
                sp.latex(solution)
            )

        except Exception as e:

            st.error(
                "Unable to solve this equation. "
                "Try an expression such as x*y."
            )


# ================================================================
# LINEAR ODE
# ================================================================

elif topic == "Linear ODE":

    st.header("3. First Order Linear Differential Equation")

    st.write(
        "The standard form of a first-order linear ODE is:"
    )

    st.latex(r"""
    \frac{dy}{dx}+P(x)y=Q(x)
    """)

    st.subheader("Integrating Factor")

    st.latex(r"""
    IF=e^{\int P(x)\,dx}
    """)

    st.subheader("Solution Formula")

    st.latex(r"""
    y(IF)=\int Q(x)(IF)\,dx+C
    """)

    st.divider()

    st.subheader("Example")

    st.latex(r"""
    \frac{dy}{dx}+2y=e^x
    """)

    st.latex(r"""
    P(x)=2
    """)

    st.latex(r"""
    IF=e^{\int2dx}=e^{2x}
    """)

    st.latex(r"""
    ye^{2x}
    =
    \int e^xe^{2x}dx+C
    """)

    st.latex(r"""
    y=\frac{1}{3}e^x+Ce^{-2x}
    """)


# ================================================================
# BERNOULLI
# ================================================================

elif topic == "Bernoulli Equation":

    st.header("4. Bernoulli Differential Equation")

    st.write(
        """
        A Bernoulli equation has the form:
        """
    )

    st.latex(r"""
    \frac{dy}{dx}+P(x)y=Q(x)y^n
    """)

    st.write("Put")

    st.latex(r"""
    v=y^{1-n}
    """)

    st.write("Then the equation becomes linear.")

    st.latex(r"""
    \frac{dv}{dx}+(1-n)P(x)v
    =
    (1-n)Q(x)
    """)

    st.subheader("Example")

    st.latex(r"""
    \frac{dy}{dx}+y=xy^2
    """)

    st.write("Here")

    st.latex(r"""
    P(x)=1,\quad Q(x)=x,\quad n=2
    """)

    st.write("Substitute")

    st.latex(r"""
    v=y^{-1}
    """)

    st.write("The equation can then be solved as a linear ODE.")


# ================================================================
# EULER METHOD
# ================================================================

elif topic == "Euler Numerical Method":

    st.header("5. Euler Numerical Method")

    st.write(
        """
        Euler's method is a numerical method for solving a
        first-order initial value problem:
        """
    )

    st.latex(r"""
    \frac{dy}{dx}=f(x,y)
    """)

    st.latex(r"""
    y_{n+1}=y_n+h f(x_n,y_n)
    """)

    st.divider()

    f_text = st.text_input(
        "Enter f(x,y)",
        "x + y"
    )

    x0 = st.number_input(
        "Initial x",
        value=0.0
    )

    y0 = st.number_input(
        "Initial y",
        value=1.0
    )

    h = st.number_input(
        "Step size h",
        value=0.1
    )

    n = st.number_input(
        "Number of steps",
        min_value=1,
        max_value=1000,
        value=10
    )

    if st.button("Run Euler Method"):

        try:

            f_expr = sp.sympify(f_text)

            f_func = sp.lambdify(
                (x, y),
                f_expr,
                "numpy"
            )

            xs = [x0]
            ys = [y0]

            for i in range(int(n)):

                x_current = xs[-1]
                y_current = ys[-1]

                y_new = (
                    y_current
                    +
                    h * f_func(
                        x_current,
                        y_current
                    )
                )

                x_new = x_current + h

                xs.append(x_new)
                ys.append(float(y_new))

            st.subheader("Numerical Results")

            data = {
                "x": xs,
                "y": ys
            }

            st.dataframe(data)

            fig, ax = plt.subplots()

            ax.plot(xs, ys, marker="o")

            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_title("Euler Method")

            ax.grid()

            st.pyplot(fig)

        except Exception:

            st.error(
                "Invalid function. Example: x+y"
            )


# ================================================================
# RUNGE KUTTA
# ================================================================

elif topic == "Runge-Kutta Method":

    st.header("6. Fourth Order Runge-Kutta Method")

    st.write(
        "The classical fourth-order Runge-Kutta method uses:"
    )

    st.latex(r"""
    k_1=f(x_n,y_n)
    """)

    st.latex(r"""
    k_2=f(x_n+h/2,y_n+hk_1/2)
    """)

    st.latex(r"""
    k_3=f(x_n+h/2,y_n+hk_2/2)
    """)

    st.latex(r"""
    k_4=f(x_n+h,y_n+hk_3)
    """)

    st.latex(r"""
    y_{n+1}
    =
    y_n+
    \frac{h}{6}
    (k_1+2k_2+2k_3+k_4)
    """)

    st.divider()

    f_text = st.text_input(
        "Enter f(x,y)",
        "x + y",
        key="rk_function"
    )

    x0 = st.number_input(
        "Initial x",
        value=0.0,
        key="rk_x"
    )

    y0 = st.number_input(
        "Initial y",
        value=1.0,
        key="rk_y"
    )

    h = st.number_input(
        "Step size",
        value=0.1,
        key="rk_h"
    )

    n = st.number_input(
        "Number of steps",
        min_value=1,
        max_value=1000,
        value=10,
        key="rk_n"
    )

    if st.button("Run RK4"):

        try:

            f_expr = sp.sympify(f_text)

            f_func = sp.lambdify(
                (x, y),
                f_expr,
                "numpy"
            )

            xs = [x0]
            ys = [y0]

            for i in range(int(n)):

                xn = xs[-1]
                yn = ys[-1]

                k1 = f_func(xn, yn)

                k2 = f_func(
                    xn + h / 2,
                    yn + h * k1 / 2
                )

                k3 = f_func(
                    xn + h / 2,
                    yn + h * k2 / 2
                )

                k4 = f_func(
                    xn + h,
                    yn + h * k3
                )

                yn1 = yn + (
                    h / 6
                ) * (
                    k1 + 2*k2 + 2*k3 + k4
                )

                xs.append(xn + h)
                ys.append(float(yn1))

            st.subheader("Numerical Results")

            st.dataframe({
                "x": xs,
                "y": ys
            })

            fig, ax = plt.subplots()

            ax.plot(
                xs,
                ys,
                marker="o"
            )

            ax.set_xlabel("x")
            ax.set_ylabel("y")

            ax.set_title(
                "Fourth Order Runge-Kutta Method"
            )

            ax.grid()

            st.pyplot(fig)

        except Exception:

            st.error(
                "Invalid function. Example: x+y"
            )


# ================================================================
# INTRODUCTION TO PDE
# ================================================================

elif topic == "Introduction to PDE":

    st.header("7. Introduction to Partial Differential Equations")

    st.write(
        """
        A partial differential equation is an equation containing
        partial derivatives of an unknown function of two or more
        independent variables.
        """
    )

    st.latex(r"""
    F(x,y,z,p,q)=0
    """)

    st.write("where")

    st.latex(r"""
    p=\frac{\partial z}{\partial x},
    \qquad
    q=\frac{\partial z}{\partial y}
    """)

    st.subheader("Example")

    st.latex(r"""
    p+q=0
    """)

    st.write(
        """
        This is a first-order PDE.
        """
    )

    st.subheader("Classification")

    st.markdown(
        """
        **First-order PDE**

        Contains first partial derivatives.

        **Linear PDE**

        The dependent variable and its derivatives occur linearly.

        **Non-linear PDE**

        The dependent variable or derivatives occur non-linearly.
        """
    )


# ================================================================
# LAGRANGE PDE
# ================================================================

elif topic == "Lagrange PDE":

    st.header("8. Lagrange's First Order PDE")

    st.write(
        """
        Lagrange's linear PDE has the form:
        """
    )

    st.latex(r"""
    Pp+Qq=R
    """)

    st.write("where")

    st.latex(r"""
    p=\frac{\partial z}{\partial x},
    \qquad
    q=\frac{\partial z}{\partial y}
    """)

    st.subheader("Auxiliary Equations")

    st.latex(r"""
    \frac{dx}{P}
    =
    \frac{dy}{Q}
    =
    \frac{dz}{R}
    """)

    st.subheader("Example")

    st.latex(r"""
    p+q=0
    """)

    st.write("Auxiliary equations:")

    st.latex(r"""
    \frac{dx}{1}
    =
    \frac{dy}{1}
    =
    \frac{dz}{0}
    """)

    st.write(
        """
        From dx = dy, we obtain:
        """
    )

    st.latex(r"""
    x-y=c_1
    """)

    st.write(
        """
        Since dz = 0:
        """
    )

    st.latex(r"""
    z=c_2
    """)


# ================================================================
# CHARPIT PDE
# ================================================================

elif topic == "Charpit PDE":

    st.header("9. Charpit's Method")

    st.write(
        """
        Charpit's method is used to solve certain non-linear
        first-order PDEs.
        """
    )

    st.latex(r"""
    F(x,y,z,p,q)=0
    """)

    st.write("Charpit's equations are based on:")

    st.latex(r"""
    \frac{dp}{-F_x-pF_z}
    =
    \frac{dq}{-F_y-qF_z}
    """)

    st.latex(r"""
    \frac{dx}{F_p}
    =
    \frac{dy}{F_q}
    """)

    st.write(
        """
        A suitable first integral is obtained from these
        auxiliary equations and substituted into the original PDE.
        """
    )

    st.subheader("Example Type")

    st.latex(r"""
    z=px+qy+f(p,q)
    """)

    st.write(
        """
        Charpit's method is particularly useful when the PDE
        cannot be directly treated by Lagrange's method.
        """
    )


# ================================================================
# LINEAR PDE
# ================================================================

elif topic == "Linear PDE":

    st.header("10. Linear Partial Differential Equations")

    st.write(
        """
        A linear PDE contains the dependent variable and its
        derivatives only to the first degree.
        """
    )

    st.subheader("First Order Linear PDE")

    st.latex(r"""
    Pp+Qq=R
    """)

    st.write(
        """
        This is solved using Lagrange's auxiliary equations.
        """
    )

    st.latex(r"""
    \frac{dx}{P}
    =
    \frac{dy}{Q}
    =
    \frac{dz}{R}
    """)

    st.subheader("Second Order Linear PDE")

    st.latex(r"""
    A\frac{\partial^2z}{\partial x^2}
    +
    2B\frac{\partial^2z}{\partial x\partial y}
    +
    C\frac{\partial^2z}{\partial y^2}
    =F
    """)

    st.write("Classification depends on:")

    st.latex(r"""
    B^2-AC
    """)

    st.markdown(
        """
        - B² − AC > 0 → Hyperbolic
        - B² − AC = 0 → Parabolic
        - B² − AC < 0 → Elliptic
        """
    )


# ================================================================
# NON-LINEAR PDE
# ================================================================

elif topic == "Non-Linear PDE":

    st.header("11. Non-Linear Partial Differential Equations")

    st.write(
        """
        A PDE is non-linear when the dependent variable or its
        derivatives occur non-linearly.
        """
    )

    st.subheader("General First Order PDE")

    st.latex(r"""
    F(x,y,z,p,q)=0
    """)

    st.subheader("Important Methods")

    st.markdown(
        """
        ### 1. Charpit's Method

        Used for many non-linear first-order PDEs.

        ### 2. Complete Integral

        A solution containing two arbitrary constants.

        ### 3. Singular Integral

        Obtained by eliminating the arbitrary constants from
        the complete integral.
        """
    )

    st.subheader("Example")

    st.latex(r"""
    z=px+qy+pq
    """)

    st.write(
        """
        This is a non-linear first-order PDE because p and q
        occur as a product.
        """)


# ================================================================
# ABOUT
# ================================================================

elif topic == "About Project":

    st.header("12. About the Project")

    st.write(
        """
        ### Differential Equations Toolkit

        This project was developed as an educational Python
        application for mathematics students.

        It combines mathematical theory with computational tools.
        """
    )

    st.subheader("Topics Covered")

    topics = [
        "Introduction to Differential Equations",
        "Ordinary Differential Equations",
        "First Order ODE",
        "Linear ODE",
        "Bernoulli Equation",
        "Euler Numerical Method",
        "Runge-Kutta Method",
        "Partial Differential Equations",
        "Lagrange's Method",
        "Charpit's Method",
        "Linear PDE",
        "Non-Linear PDE"
    ]

    for item in topics:
        st.write("✓", item)

    st.subheader("Libraries Used")

    st.code(
        """
SymPy
NumPy
Matplotlib
Streamlit
        """
    )

    st.success(
        "Developed as a mathematics-oriented computational project."
    )


# ================================================================
# FOOTER
# ================================================================

st.sidebar.markdown("---")
st.sidebar.write(
    "Differential Equations Toolkit"
)
st.sidebar.write(
    "Python + SymPy + NumPy + Matplotlib + Streamlit"
)