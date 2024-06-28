import React, { useState } from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { Link, useNavigate } from 'react-router-dom';

const validationSchema = Yup.object({
  full_name: Yup.string()
    .min(3, 'Full name must be at least 3 characters')
    .required('Required'),
  email: Yup.string()
    .email('Invalid email address')
    .required('Required'),
  password: Yup.string()
    .min(6, 'Password must be at least 6 characters')
    .matches(/[a-zA-Z]/, 'Password must contain a letter')
    .matches(/\d/, 'Password must contain a number')
    .matches(/[!@#$%^&*(),.?":{}|<>]/, 'Password must contain a special character')
    .required('Required'),
});

function Signup() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const formik = useFormik({
    initialValues: {
      full_name: '',
      email: '',
      password: '',
    },
    validationSchema,
    onSubmit: async (values) => {
      setLoading(true);
      setError(null);

      try {
        const response = await fetch('http://127.0.0.1:8001/auth/users/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(values),
        });

        if (!response.ok) {
          const res = await response.json()
          console.log("response is signup :: ", res)
          throw new Error(res['detail']);
        }

        navigate('/login');
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
        <h2 className="card-title">Sign Up</h2>
        <form onSubmit={formik.handleSubmit}>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Full Name</span>
            </label>
            <input
              type="text"
              name="full_name"
              value={formik.values.full_name}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              className="input input-bordered"
              required
            />
            {formik.touched.full_name && formik.errors.full_name ? (
              <div className="text-red-500 text-sm">{formik.errors.full_name}</div>
            ) : null}
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Email</span>
            </label>
            <input
              type="email"
              name="email"
              value={formik.values.email}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              className="input input-bordered"
              required
            />
            {formik.touched.email && formik.errors.email ? (
              <div className="text-red-500 text-sm">{formik.errors.email}</div>
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
              {loading ? 'Signing up...' : 'Sign Up'}
            </button>
          </div>
        </form>
        {error && (
          <div className="alert alert-error mt-4">
            <span>{error}</span>
          </div>
        )}
        <div className="mt-4">
          <p>Already have an account? <Link to="/login" className="text-blue-500">Login here</Link></p>
        </div>
      </div>
    </div>
  );
}

export default Signup;
