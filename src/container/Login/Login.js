import './Login.css'

const Login = () => {

    return (
        <>
            <div className="login">
                <h2 className="active"> sign in </h2>

                <h2 className="nonactive"> sign up </h2>
                <form action='/login' method="POST">
                    <input type="text" className="text" name="email" />
                    <span>username</span>
                    <br />
                    <br />
                    <input type="password" className="text" name="password" />
                    <span>password</span>
                    <br />

                    <input type="checkbox" id="checkbox-1-1" className="custom-checkbox"/>
                    <label htmlFor="checkbox-1-1">Keep me Signed in</label>

                    <button className="signin" type="submit">
                        Sign In
                    </button>
                    <hr />
                        <a href="#">Forgot Password?</a>
                </form>
            </div>
        </>
    )
}

export default Login;