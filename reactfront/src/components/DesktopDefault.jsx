import PropTypes from "prop-types";

const DesktopDefault = ({ className = "", default1, addressValue }) => {
  return (
    <div
      className={`flex-1 flex flex-col items-start justify-start gap-[4px] min-w-[372px] max-w-full text-left text-xs text-light-theme-text-primary-body font-subtitle-1 mq450:min-w-full ${className}`}
    >
      <div className="self-stretch relative tracking-[0.4px] leading-[16px]">
        {default1}
      </div>
      <div className="self-stretch rounded bg-light-theme-background-bg box-border flex flex-row items-center justify-start py-0 pr-0 pl-3.5 max-w-full text-base text-lightgray border-[1px] border-solid border-light-theme-border-and-divider-border-and-divider">
        <div className="hidden flex-row items-center justify-start py-2 pr-2 pl-0">
          <img
            className="h-6 w-6 relative overflow-hidden shrink-0"
            alt=""
            src="/icon.svg"
          />
        </div>
        <div className="flex-1 flex flex-row items-center justify-start py-2.5 px-0 box-border max-w-full">
          <div className="flex flex-row items-center justify-start">
            <div className="relative tracking-[0.2px] leading-[20px] inline-block min-w-[88px]">
              {addressValue}
            </div>
          </div>
        </div>
        <div className="hidden flex-row items-center justify-start py-2 pr-4 pl-0">
          <img
            className="h-6 w-6 relative overflow-hidden shrink-0"
            alt=""
            src="/icon.svg"
          />
        </div>
      </div>
    </div>
  );
};

DesktopDefault.propTypes = {
  className: PropTypes.string,
  default1: PropTypes.string,
  addressValue: PropTypes.string,
};

export default DesktopDefault;
