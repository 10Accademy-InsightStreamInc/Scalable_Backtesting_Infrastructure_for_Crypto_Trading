import PropTypes from "prop-types";

const Auth0FormsLogin = ({ className = "" }) => {
  return (
    <div
      className={`w-[402px] shadow-[0px_20px_25px_-5px_rgba(0,_0,_0,_0.1),_0px_10px_10px_-5px_rgba(0,_0,_0,_0.04)] rounded-md bg-white-background-primary overflow-hidden shrink-0 flex flex-col items-start justify-start p-12 box-border gap-[24px] max-w-full text-center text-base text-text-primary font-subtitle-1 mq450:pl-5 mq450:pr-5 mq450:box-border mq525:pt-[31px] mq525:pb-[31px] mq525:box-border ${className}`}
    >
      <h3 className="m-0 self-stretch relative text-5xl tracking-[0.18px] leading-[24px] font-normal font-poetsenone mq450:text-lgi mq450:leading-[19px]">
        <p className="m-0">Welcome To</p>
        <p className="m-0">Crypto Back Testing</p>
        <p className="m-0">Platform</p>
      </h3>
      <img className="w-56 h-12 relative hidden" alt="" src="/logo.svg" />
      <div className="self-stretch relative tracking-[0.18px] leading-[24px] font-light">
        Input Your Email and Password to Continue
      </div>
      <div className="w-[328px] h-[22px] hidden flex-row items-center justify-start py-0 px-4 box-border max-w-full text-left text-xs text-textsecondary">
        <div className="h-4 flex-1 relative tracking-[0.4px] leading-[16px] inline-block">
          Assistive text
        </div>
      </div>
      <div className="self-stretch flex flex-col items-start justify-start gap-[16px] text-left text-xs text-textsecondary">
        <div className="self-stretch flex flex-col items-start justify-start gap-[24px]">
          <div className="self-stretch h-14 rounded box-border flex flex-col items-end justify-start py-4 px-0 gap-[4px] border-[1px] border-solid border-border">
            <div className="mt-[-26px] self-stretch flex flex-row items-start justify-start py-0 px-3">
              <div className="bg-white-background-primary flex flex-row items-start justify-start py-[3px] px-1 whitespace-nowrap">
                <div className="relative tracking-[0.4px] leading-[16px] inline-block min-w-[81px]">
                  Email address
                </div>
              </div>
            </div>
            <input
              className="w-full [border:none] [outline:none] bg-[transparent] self-stretch h-6 flex flex-row items-start justify-end py-0 px-4 box-border font-subtitle-1 font-medium text-base text-text-primary min-w-[184px] shrink-0"
              placeholder="martin@company.com"
              type="text"
            />
          </div>
          <div className="self-stretch flex flex-row items-start justify-start text-base text-text-primary">
            <div className="h-14 flex-1 rounded box-border flex flex-col items-end justify-start py-4 px-0 gap-[4px] border-[2px] border-solid border-link">
              <div className="mt-[-26px] self-stretch h-[22px] flex flex-row items-start justify-start py-0 px-3 box-border min-w-[184px] shrink-0">
                <div className="h-[22px] w-16 bg-white-background-primary flex flex-row items-start justify-start p-[3px] box-border">
                  <input
                    className="w-[57px] [border:none] [outline:none] font-subtitle-1 text-xs bg-[transparent] h-4 relative tracking-[0.4px] leading-[16px] text-link text-left inline-block"
                    placeholder="Password"
                    type="text"
                  />
                </div>
              </div>
              <div className="self-stretch h-6 flex flex-row items-start justify-end py-0 pr-3 pl-4 box-border shrink-0">
                <div className="self-stretch flex-1 flex flex-row items-start justify-between gap-[20px]">
                  <div className="self-stretch w-[5px] flex flex-row items-start justify-start gap-[4px]">
                    <div className="self-stretch flex-1 relative tracking-[0.15px] leading-[24px] font-medium" />
                    <div className="flex flex-col items-start justify-start pt-[3.5px] px-0 pb-0">
                      <div className="w-px h-[17px] relative bg-primary-500" />
                    </div>
                  </div>
                  <div className="flex flex-row items-start justify-start gap-[8px] text-right text-link">
                    <img
                      className="h-6 w-6 relative object-cover"
                      alt=""
                      src="/trailing-icon@2x.png"
                    />
                    <div className="self-stretch w-7 relative tracking-[0.15px] leading-[24px] font-medium hidden">
                      Edit
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="h-[22px] w-[328px] hidden flex-row items-center justify-start py-0 px-4 box-border max-w-full text-xs text-link">
              <div className="flex-1 relative tracking-[0.4px] leading-[16px]">
                Assistive text
              </div>
            </div>
          </div>
        </div>
        <div className="self-stretch relative text-base tracking-[0.15px] leading-[24px] font-medium text-cta-color">
          Forgot password?
        </div>
      </div>
      <button className="cursor-pointer [border:none] py-[13px] px-5 bg-cta-color self-stretch shadow-[0px_1px_2px_rgba(0,_0,_0,_0.05)] rounded-sm flex flex-row items-start justify-center hover:bg-mediumslateblue">
        <div className="relative text-base leading-[24px] font-medium font-label-base-16-24 text-white-background-primary text-center inline-block min-w-[70px]">
          Continue
        </div>
      </button>
      <div className="flex flex-row items-start justify-start gap-[8px]">
        <div className="relative tracking-[0.15px] leading-[24px] font-medium">
          Don’t have an account?
        </div>
        <div className="relative tracking-[0.15px] leading-[24px] font-medium text-cta-color inline-block min-w-[55px] whitespace-nowrap">
          Sign up
        </div>
      </div>
    </div>
  );
};

Auth0FormsLogin.propTypes = {
  className: PropTypes.string,
};

export default Auth0FormsLogin;
//1-103 working