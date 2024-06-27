import React, { useState } from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { Link, useNavigate } from 'react-router-dom';

const validationSchema = Yup.object({
  username: Yup.string()
    .min(3, 'Username must be at least 3 characters')
    .required('Required'),
  password: Yup.string()
    .min(6, 'Password must be at least 6 characters')
    .matches(/[a-zA-Z]/, 'Password must contain a letter')
    .matches(/\d/, 'Password must contain a number')
    .matches(/[!@#$%^&*(),.?":{}|<>]/, 'Password must contain a special character')
    .required('Required'),
});

function Login() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const formik = useFormik({
    initialValues: {
      username: '',
      password: '',
    },
    validationSchema,
    onSubmit: async (values) => {
      setLoading(true);
      setError(null);

      const formData = new FormData();
      formData.append('username', values.username);
      formData.append('password', values.password);

      try {
        const response = await fetch('http://127.0.0.1:8001/auth/token', {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          throw new Error('Invalid username or password');
        }

        const data = await response.json();
        console.log("The data from login :: ", data)
        localStorage.setItem('token', data.access_token);
        navigate('/backtest');
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    },
  });

  return (
    <div className="card bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">Login</h2>
        <form onSubmit={formik.handleSubmit}>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Username</span>
            </label>
            <input
              type="text"
              name="username"
              value={formik.values.username}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              className="input input-bordered"
              required
            />
            {formik.touched.username && formik.errors.username ? (
              <div className="text-red-500 text-sm">{formik.errors.username}</div>
            ) : null}
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Password</span>
            </label>
            <input
              type="password"
              name="password"
              value={formik.values.password}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              className="input input-bordered"
              required
            />
            {formik.touched.password && formik.errors.password ? (
              <div className="text-red-500 text-sm">{formik.errors.password}</div>
            ) : null}
          </div>
          <div className="form-control mt-4">
            <button type="submit" className="btn btn-primary bg-neutral-600" style={{ color: 'white' }} disabled={loading}>
              {loading ? 'Logging in...' : 'Login'}
            </button>
          </div>
        </form>
        {error && (
          <div className="alert alert-error mt-4">
            <span>{error}</span>
          </div>
        )}
        <div className="mt-4">
          <p>Don't have an account? <Link to="/signup" className="text-blue-500">Sign up here</Link></p>
        </div>
      </div>
    </div>
  );
}

export default Login;
