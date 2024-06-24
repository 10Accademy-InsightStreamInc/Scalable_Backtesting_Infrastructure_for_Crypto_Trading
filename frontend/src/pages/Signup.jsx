import Auth0FormsSignup from "../components/Auth0FormsSignup";

const Signup = () => {
  return (
    <div className="w-full h-[982px] relative bg-white-background-primary overflow-hidden flex flex-row items-start justify-end pt-[216px] px-[491px] pb-[244px] box-border leading-[normal] tracking-[normal] lg:pl-[245px] lg:pr-[245px] lg:box-border mq450:pl-5 mq450:pr-5 mq450:box-border mq750:pl-[122px] mq750:pr-[122px] mq750:box-border">
      <Auth0FormsSignup />
    </div>
  );
};

export default Signup;
