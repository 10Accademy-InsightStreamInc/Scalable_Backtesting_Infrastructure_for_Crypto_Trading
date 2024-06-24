import Auth0FormsLogin from "../components/Auth0FormsLogin";

const Login = () => {
  return (
    <div className="w-full h-[982px] relative bg-white-background-primary overflow-hidden flex flex-row items-start justify-center py-[210px] px-5 box-border leading-[normal] tracking-[normal]">
      <Auth0FormsLogin />
    </div>
  );
};

export default Login;
