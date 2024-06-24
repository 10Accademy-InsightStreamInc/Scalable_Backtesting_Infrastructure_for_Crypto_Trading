import PropTypes from "prop-types";

const Auth0FormsSignup = ({ className = "" }) => {
  return (
    <div
      className={`w-[402px] shadow-[0px_20px_25px_-5px_rgba(0,_0,_0,_0.1),_0px_10px_10px_-5px_rgba(0,_0,_0,_0.04)] rounded-md bg-white-background-primary flex flex-col items-start justify-start p-12 box-border gap-[24px] max-w-full text-center text-base text-text-primary font-subtitle-1 mq450:pl-5 mq450:pr-5 mq450:box-border mq750:pt-[31px] mq750:pb-[31px] mq750:box-border ${className}`}
    >
      <h3 className="m-0 self-stretch relative text-5xl tracking-[0.18px] leading-[24px] font-normal font-poetsenone mq450:text-lgi mq450:leading-[19px]">
        <p className="m-0">Welcome To</p>
        <p className="m-0">Crypto Back Testing</p>
        <p className="m-0">Platform</p>
      </h3>
      <img className="w-56 h-12 relative hidden" alt="" src="/logo.svg" />
      <div className="self-stretch relative tracking-[0.18px] leading-[24px] font-light">
        It Only Takes a Second to Have Your Account Ready!
      </div>
      <div className="self-stretch rounded flex flex-row items-start justify-start py-3.5 pr-[11px] pl-[15px] text-left text-xs text-link border-[1px] border-solid border-border">
        <input
          className="w-full [border:none] [outline:none] bg-[transparent] h-6 flex-1 flex flex-row items-start justify-start font-subtitle-1 font-medium text-base text-textsecondary min-w-[167px]"
          placeholder="Email address"
          type="text"
        />
        <div className="w-[306px] hidden flex-row items-center justify-start py-0 pr-[11px] pl-3 box-border">
          <div className="h-[22px] bg-white-background-primary flex flex-row items-center justify-start py-0 px-1 box-border">
            <div className="relative tracking-[0.4px] leading-[16px]">
              Label
            </div>
          </div>
        </div>
      </div>
      <div className="w-[328px] h-[22px] hidden flex-row items-center justify-start py-0 px-4 box-border max-w-full text-left text-xs text-textsecondary">
        <div className="h-4 flex-1 relative tracking-[0.4px] leading-[16px] inline-block">
          Assistive text
        </div>
      </div>
      <div className="self-stretch h-14 rounded box-border flex flex-col items-end justify-start py-4 px-0 gap-[4px] text-left border-[2px] border-solid border-link">
        <div className="mt-[-26px] self-stretch h-[22px] flex flex-row items-start justify-start py-0 px-3 box-border min-w-[184px] shrink-0">
          <div className="h-[22px] w-16 bg-white-background-primary flex flex-row items-start justify-start p-[3px] box-border">
            <input
              className="w-[57px] [border:none] [outline:none] font-subtitle-1 text-xs bg-[transparent] h-4 relative tracking-[0.4px] leading-[16px] text-link text-left inline-block"
              placeholder="Password"
              type="text"
            />
          </div>
        </div>
        <div className="self-stretch flex flex-row items-start justify-end py-0 pr-3 pl-4">
          <div className="flex-1 flex flex-row items-start justify-between gap-[20px]">
            <div className="flex flex-col items-start justify-start pt-[3.5px] px-0 pb-0">
              <div className="flex flex-row items-center justify-start gap-[4px]">
                <div className="h-6 w-[245px] relative tracking-[0.15px] leading-[24px] font-medium hidden whitespace-nowrap">
                  max.mustermann@company.com
                </div>
                <div className="h-[17px] w-px relative bg-primary-500" />
              </div>
            </div>
            <div className="flex flex-row items-start justify-start text-right text-primary-color">
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
      <button className="cursor-pointer [border:none] py-[13px] px-5 bg-cta-color self-stretch shadow-[0px_1px_2px_rgba(0,_0,_0,_0.05)] rounded-sm flex flex-row items-start justify-center whitespace-nowrap hover:bg-mediumslateblue">
        <div className="relative text-base leading-[24px] font-medium font-label-base-16-24 text-white-background-primary text-center inline-block min-w-[120px]">
          Create Account
        </div>
      </button>
      <div className="flex flex-row items-start justify-start gap-[8px] top-[0] z-[99] sticky">
        <div className="relative tracking-[0.15px] leading-[24px] font-medium whitespace-nowrap">
          Already have an account?
        </div>
        <div className="relative tracking-[0.15px] leading-[24px] font-medium text-cta-color inline-block min-w-[41px]">
          Login
        </div>
      </div>
    </div>
  );
};

Auth0FormsSignup.propTypes = {
  className: PropTypes.string,
};

export default Auth0FormsSignup;
