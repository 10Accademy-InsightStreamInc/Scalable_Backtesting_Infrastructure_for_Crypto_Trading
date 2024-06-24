import { useMemo } from "react";
import PropTypes from "prop-types";

const DesktopDefault1 = ({
  className = "",
  default1,
  contentPlaceholder,
  propAlignSelf,
  propFlex,
}) => {
  const desktopDefaultStyle = useMemo(() => {
    return {
      alignSelf: propAlignSelf,
      flex: propFlex,
    };
  }, [propAlignSelf, propFlex]);

  return (
    <div
      className={`self-stretch flex flex-col items-start justify-start gap-[4px] max-w-full text-left text-xs text-light-theme-text-primary-body font-subtitle-1 ${className}`}
      style={desktopDefaultStyle}
    >
      <div className="self-stretch relative tracking-[0.4px] leading-[16px]">
        {default1}
      </div>
      <div className="self-stretch rounded bg-light-theme-background-bg box-border flex flex-row items-center justify-start py-0 pr-0 pl-3.5 max-w-full border-[1px] border-solid border-light-theme-border-and-divider-border-and-divider">
        <div className="hidden flex-row items-center justify-start py-2 pr-2 pl-0">
          <img
            className="h-6 w-6 relative overflow-hidden shrink-0"
            alt=""
            src="/icon.svg"
          />
        </div>
        <input
          className="w-full [border:none] [outline:none] bg-[transparent] h-10 flex-1 flex flex-row items-center justify-start py-2.5 px-0 box-border font-subtitle-1 text-base text-lightgray min-w-[250px] max-w-full"
          placeholder={contentPlaceholder}
          type="text"
        />
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

DesktopDefault1.propTypes = {
  className: PropTypes.string,
  default1: PropTypes.string,
  contentPlaceholder: PropTypes.string,

  /** Style props */
  propAlignSelf: PropTypes.any,
  propFlex: PropTypes.any,
};

export default DesktopDefault1;
