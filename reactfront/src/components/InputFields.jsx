import DesktopDefault1 from "./DesktopDefault1";
import DesktopDefault from "./DesktopDefault";
import PropTypes from "prop-types";

const InputFields = ({ className = "" }) => {
  return (
    <div
      className={`self-stretch flex flex-col items-start justify-start gap-[24px] max-w-full text-left text-5xl text-light-theme-text-primary-body font-subtitle-1 ${className}`}
    >
      <div className="self-stretch flex flex-col items-start justify-start gap-[28px] max-w-full text-13xl">
        <div className="self-stretch flex flex-row items-start justify-between max-w-full gap-[20px] mq675:flex-wrap">
          <div className="flex flex-col items-start justify-start pt-px px-0 pb-0">
            <div className="flex flex-row items-start justify-start gap-[8px]">
              <img
                className="h-10 w-10 relative rounded-sm overflow-hidden shrink-0 object-cover min-h-[40px]"
                loading="lazy"
                alt=""
                src="/avatar@2x.png"
              />
              <a className="[text-decoration:none] relative leading-[40px] font-semibold text-[inherit] mq450:text-lgi mq450:leading-[24px] mq900:text-7xl mq900:leading-[32px]">
                John Johnson
              </a>
            </div>
          </div>
          <div className="w-[328px] flex flex-row items-start justify-start gap-[16px] max-w-full text-base">
            <div className="flex-1 rounded bg-light-theme-background-bg flex flex-row items-start justify-start py-2.5 px-[63px] gap-[24px] border-[1px] border-solid border-light-theme-border-and-divider-border-and-divider mq450:pl-5 mq450:pr-5 mq450:box-border">
              <div className="flex flex-row items-start justify-start gap-[8px]">
                <img
                  className="h-6 w-6 relative rounded-sm overflow-hidden shrink-0 object-cover min-h-[24px]"
                  loading="lazy"
                  alt=""
                  src="/avatar-1@2x.png"
                />
                <div className="flex flex-col items-start justify-start pt-0.5 px-0 pb-0">
                  <a className="[text-decoration:none] relative tracking-[0.15px] leading-[20px] font-medium text-[inherit] inline-block min-w-[104px]">
                    John Johnson
                  </a>
                </div>
              </div>
              <img
                className="h-6 w-6 relative hidden min-h-[24px]"
                alt=""
                src="/short-arrow.svg"
              />
            </div>
            <div className="h-12 w-12 rounded bg-light-theme-background-bg box-border flex flex-row items-center justify-center p-3 relative gap-[8px] text-center text-2xs text-white-background-primary border-[1px] border-solid border-light-theme-border-and-divider-border-and-divider">
              <img
                className="h-6 w-6 absolute !m-[0] top-[12px] left-[12px]"
                loading="lazy"
                alt=""
                src="/notification.svg"
              />
              <div className="w-4 !m-[0] absolute top-[5px] left-[26px] rounded bg-color-variants-purple-5 overflow-hidden shrink-0 flex flex-row items-start justify-start p-px box-border z-[1]">
                <a className="[text-decoration:none] flex-1 relative tracking-[0.5px] leading-[16px] font-medium text-[inherit]">
                  3
                </a>
              </div>
            </div>
          </div>
        </div>
        <div className="self-stretch h-px relative rounded-31xl bg-light-theme-border-and-divider-border-and-divider overflow-hidden shrink-0" />
      </div>
      <div className="self-stretch flex flex-row flex-wrap items-start justify-start gap-[48px] max-w-full mq675:gap-[24px]">
        <div className="flex-1 flex flex-col items-start justify-start gap-[16px] min-w-[372px] max-w-full mq450:min-w-full">
          <div className="flex flex-col items-start justify-start gap-[8px]">
            <h3 className="m-0 relative text-inherit leading-[32px] font-medium font-inherit mq450:text-lgi mq450:leading-[26px]">
              Choose Your Stock
            </h3>
            <div className="relative text-base tracking-[0.2px] leading-[20px]">{`Choose The Stock Name `}</div>
          </div>
          <div className="self-stretch flex flex-col items-start justify-start gap-[4px] max-w-full text-xs">
            <div className="self-stretch relative tracking-[0.4px] leading-[16px]">
              Stock
            </div>
            <div className="self-stretch rounded bg-light-theme-background-bg box-border flex flex-row items-center justify-start py-0 pr-[7px] pl-4 max-w-full [row-gap:20px] text-base text-lightgray border-[1px] border-solid border-light-theme-border-and-divider-border-and-divider mq675:flex-wrap">
              <div className="hidden flex-row items-center justify-start py-2 pr-2 pl-0">
                <img
                  className="h-6 w-6 relative overflow-hidden shrink-0"
                  alt=""
                  src="/icon.svg"
                />
              </div>
              <div className="flex-1 flex flex-row items-center justify-start py-2.5 px-0 box-border min-w-[46px] max-w-full">
                <div className="flex flex-row items-center justify-start">
                  <a className="[text-decoration:none] relative tracking-[0.2px] leading-[20px] text-[inherit] inline-block min-w-[46px]">
                    Nvidia
                  </a>
                </div>
              </div>
              <img className="h-6 w-6 relative" alt="" src="/short-arrow.svg" />
              <div className="hidden flex-row items-center justify-start py-2 pr-4 pl-0">
                <img
                  className="h-6 w-6 relative overflow-hidden shrink-0"
                  alt=""
                  src="/icon.svg"
                />
              </div>
            </div>
          </div>
        </div>
        <div className="flex-1 flex flex-col items-start justify-start gap-[16px] min-w-[372px] max-w-full mq450:min-w-full">
          <div className="flex flex-col items-start justify-start gap-[8px]">
            <a className="[text-decoration:none] relative leading-[32px] font-medium text-[inherit] inline-block min-w-[69px] mq450:text-lgi mq450:leading-[26px]">
              Metric
            </a>
            <div className="relative text-base tracking-[0.2px] leading-[20px]">
              {" "}
              Choose the Metric
            </div>
          </div>
          <DesktopDefault1 default1="Metric" contentPlaceholder="RSI" />
        </div>
      </div>
      <div className="self-stretch flex flex-col items-start justify-start gap-[16px] max-w-full">
        <h3 className="m-0 relative text-inherit leading-[32px] font-medium font-inherit mq450:text-lgi mq450:leading-[26px]">
          Choose Start and End Date
        </h3>
        <div className="self-stretch flex flex-row flex-wrap items-start justify-start gap-[48px] max-w-full text-xs mq675:gap-[24px]">
          <DesktopDefault default1="Start Date" addressValue="12/01/2023" />
          <DesktopDefault default1="End Date" addressValue="12/01/2024" />
        </div>
      </div>
      <div className="self-stretch flex flex-col items-start justify-start gap-[16px] max-w-full">
        <h3 className="m-0 relative text-inherit leading-[32px] font-medium font-inherit inline-block min-w-[94px] mq450:text-lgi mq450:leading-[26px]">
          Portfolio
        </h3>
        <div className="self-stretch flex flex-row items-start justify-start max-w-full mq675:gap-[24px]">
          <div className="flex-1 flex flex-col items-start justify-start max-w-full">
            <div className="self-stretch flex flex-row items-start justify-start max-w-full">
              <DesktopDefault1
                default1="Start Budget"
                contentPlaceholder="$ 80,000"
                propAlignSelf="unset"
                propFlex="1"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

InputFields.propTypes = {
  className: PropTypes.string,
};

export default InputFields;
